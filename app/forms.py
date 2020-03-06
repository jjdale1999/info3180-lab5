from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,TextAreaField,SelectField
from wtforms.validators import DataRequired, Email

from wtforms import PasswordField
from wtforms.validators import InputRequired
class CreateProfile(FlaskForm):
    fname = StringField('Name', validators=[DataRequired()])
    lname = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Name', validators=[DataRequired()])
    gender = SelectField('Gender',choices=[('male','Male'),('female','Female')])
    biography = TextAreaField('Message',validators=[DataRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','Images Only'])])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

#     1. Text fields for firstname, lastname, email, location.
# 2. Select (option) field for gender (whether Male or Female)
# 3. Textarea field for a short biography.
# 4. File upload field called photo which accepts the profile image