from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, FileField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileAllowed


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=1, max=128)]) 
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=1, max=64)])
    submit = SubmitField(label="Log In")


class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=1, max=128)])
    email = EmailField(label='Email', validators=[DataRequired(), Length(max=128)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=1, max=64)])
    confirm_password = PasswordField(label='Confirm password', 
        validators=[EqualTo('password', message='Пароли должны совпадать')])
    submit = SubmitField(label="Register")


class ProfileEditForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=1, max=128)])
    email = EmailField(label='Email', validators=[DataRequired(), Length(max=128)])
    image = FileField(label='Change profile photo', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField(label="Save changes")
