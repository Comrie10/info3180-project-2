from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField, DateField, PasswordField, HiddenField
from flask_wtf.file import FileAllowed
from werkzeug.datastructures import FileStorage
from wtforms.validators import DataRequired, Email, EqualTo

class Login(FlaskForm):
    username = StringField("Username", validator=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])

class User_Name(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])

class SignUp(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    photo = FileField("Browse", validators=[FileAllowed(['jpg','png'])])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    date_of_birth = DateField("Date of Birth", validators=[DataRequired()])
    Gender = HiddenField("Gender", validators=[DataRequired()])
    password = PasswordField("New Password",validators=[DataRequired(), EqualTo("confirm",message='Password should match')])
    confirm = PasswordField('Repeat Password')

class Profile(FlaskForm):
    # auto fill name and age and the option to change photos
    description = TextAreaField("Bio")
    hobbies = TextAreaField("Hobbies/Interest")
    GEO_PREF = HiddenField("Would you prefer to use our location services", validators=[DataRequired()])
   