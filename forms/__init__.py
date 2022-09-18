from xml.dom import ValidationErr
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, RadioField
from wtforms.validators import DataRequired
import re


def username_valid(username):
    """Validates the username input"""

    #regular expression to validate the username
    userval = re.compile("\W+|_", re.I)
    match1 = userval.search(username)
    
    #validates if it was an email that was used
    userval1 = re.compile("^([a-z]+)([0-9]+)?@[a-z]+.[a-z]+", re.I)
    match2 = userval1.search(username)
    if not match1 or match2:
        return True
    return False

class User(Form):
    useremail = StringField("useremail", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    password_repeat = PasswordField("password1")
    #permission = RadioField("permission", 
    #choices=[("post:books", "creator"),
    #        ("get:books", "reader")])

    def validate(self, jump=False):
        if not username_valid(self.useremail.data):
            return False
        if jump:
            return True
        """if str(self.permission.data).lower() not in ["post:books", "get:books"]:
            return False"""
        if not self.password_repeat.data:
            return False
        if self.password.data != self.password_repeat.data:
            return False
        """self.permission.data = str(self.permission.data).split()"""
        return True

class Books(Form):
    name = StringField("books", validators=[DataRequired()])