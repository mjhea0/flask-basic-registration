# project/tests.py

import unittest
import time

from flask import current_app
from flask.ext.testing import TestCase
from flask.ext.login import current_user

from user.views import confirm_email
from project import app, db, bcrypt
from project.token import ts
from project.models import User


class BaseTestCase(TestCase):
    # Base test case.

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("ad@min.com", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])


class FlaskTestCase(BaseTestCase):

    def test_index(self):
        # Ensure Flask is setup.
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_main_route_requires_login(self):
        # Ensure main route requres logged in user.
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)


class UserViewsTests(BaseTestCase):

    def test_login_page_loads(self):
        # Ensure the login page exists.
        response = self.client.get('/login')
        self.assertIn(b'Please login', response.data)

    def test_correct_login(self):
        # Ensure login behaves correctly with correct credentials.
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin"),
                follow_redirects=True
            )
            self.assertIn(b'Welcome.', response.data)
            self.assertTrue(current_user.email == "ad@min.com")
            self.assertTrue(current_user.is_active())

    def test_incorrect_login(self):
        # Ensure login behaves correctly with incorrect credentials.
        response = self.client.post(
            '/login',
            data=dict(email="wrong@wrong.com", password="wrong"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid email and/or password.', response.data)

    def test_logout_behaves_correctly(self):
        # Ensure logout behaves correctly, regarding the session.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin"),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You were logged out', response.data)
            self.assertFalse(current_user.is_active())

    def test_logout_route_requires_login(self):
        # Ensure logout route requres logged in user.
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)

    def test_user_login_redirect(self):
        # Ensure login page redirects to main page if user is logged in.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin"),
                follow_redirects=True
            )
            response = self.client.get('/login', follow_redirects=True)
            self.assertIn(b'Welcome!', response.data)
            self.assertTrue(current_user.is_authenticated())

    def test_user_register_redirect(self):
        # Ensure register page redirects to main page if user is logged in.
        with self.client:
            self.client.post(
                '/login',
                data=dict(email="ad@min.com", password="admin"),
                follow_redirects=True
            )
            response = self.client.get('/register', follow_redirects=True)
            self.assertIn(b'Welcome!', response.data)
            self.assertTrue(current_user.is_authenticated())

    ### review! ###

    def test_password_hashing_is_random(self):
        # Ensure that password hashing is random.
        user_one = User(email="user@one.com", password='test')
        user_two = User(email="user@two.com", password='test')
        self.assertTrue(user_one.password != user_two.password)

    def test_password_verification(self):
        # Ensure password verification works correctly for user login.
        user = User(email="user@one.com", password='test')
        self.assertTrue(bcrypt.check_password_hash(user.password, "test"))
        self.assertFalse(bcrypt.check_password_hash(user.password, "non_right"))

    def test_valid_confirmation_token(self):
        # Ensure token is valid for user confirmation.
        user = User(email="user@one.com", password='test')
        db.session.add(user)
        db.session.commit()
        token = ts.dumps(user.email, salt='email-confirm-key')
        self.assertTrue(confirm_email(token))

    # def test_invalid_confirmation_token(self):
    #     user = User(email="user@one.com", password='test')
    #     db.session.add(user)
    #     db.session.commit()
    #     token = "invalid"
    #     self.assertFalse(confirm_email(token))

    # def test_expired_confirmation_token(self):
    #     user = User(email="user@one.com", password='test')
    #     db.session.add(user)
    #     db.session.commit()
    #     token = ts.dumps(user.email, salt='email-confirm-key')
    #     time.sleep(2)
    #     self.assertFalse(confirm_email(token, max_age=1))

    # # # Ensure user can register
    # def test_user_registeration(self):
    #     with self.client:
    #         response = self.client.post('/register', data=dict(
    #             email='michael@realpython.com',
    #             password='python', confirm='python'
    #         ), follow_redirects=True)
    #         self.assertIn(b'Welcome.', response.data)
    #         self.assertTrue(current_user.email == "michael@realpython.com")
    #         self.assertTrue(current_user.is_active())

if __name__ == '__main__':
    unittest.main()
