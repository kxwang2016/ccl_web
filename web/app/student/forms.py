from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, \
    TextAreaField, DateField
from wtforms.validators import Required, Optional, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User
from wtforms.fields.html5 import DateField


class NewStudentForm(Form):
    lastname = StringField('Last Name', validators=[
        Required(), Length(1, 30)])
    firstname = StringField('First Name', validators=[
        Required(), Length(1, 30)])
    middlename = StringField('Middle Name', validators=[
        Optional(), Length(0, 30)])
    chname = StringField('Chinese Name', validators=[
        Optional(), Length(0, 30)])
    birthday = DateField('Birthday', validators=[
        Required()])
    submit = SubmitField('Submit')

class RegisterSessionForm(Form):
    pass


class EditProfileForm(Form):
    lastname = StringField('Name', validators=[Length(0, 20)])
    firstname = StringField('First Name', validators=[Length(0, 20)])
    middlename = StringField('Middle Name', validators=[Length(0, 30)])
    chinesename = StringField('Chinese Name', validators=[Length(0,30)])
    submit = SubmitField('Submit')
