from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.users import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # // Modified
    # def validate_username(username):
    #     user = User.verify_username(username.data)
    #     if user is not None:
    #         raise ValidationError('Try another username')

    # // Modified
    # def validate_email(email):
    #     user = User.verify_email(email.data)
    #     if user is not None:
    #         raise ValidationError('Try another email')
