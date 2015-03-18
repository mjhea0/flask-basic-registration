# tests/test_config.py


import unittest

from flask import current_app
from flask.ext.testing import TestCase

from project import app


class TestTestingConfig(TestCase):

    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['BCRYPT_LOG_ROUNDS'] == 1)
        self.assertTrue(app.config['WTF_CSRF_ENABLED'] is False)

    def test_app_exists(self):
        self.assertFalse(current_app is None)


if __name__ == '__main__':
    unittest.main()
