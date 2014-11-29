# project/user/forms.py


from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from project.models import User


class LoginForm(Form):
    email = TextField('email', [DataRequired(), Email()])
    password = PasswordField('password', [DataRequired()])


class RegisterForm(Form):
    email = TextField(
        'email', [DataRequired(), Email(message=None), Length(min=6, max=40)])
    password = PasswordField(
        'password',
        [DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        [DataRequired(), EqualTo('password', message='Passwords must match.')]
    )

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True
