from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, FileField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileAllowed


class CreatePostForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired(), Length(max=64)]) 
    content = StringField(label='Content', validators=[DataRequired(), Length(max=516)])
    image = FileField(label='Load image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField(label="Create")
