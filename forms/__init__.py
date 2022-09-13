from flask_wtf import FlaskForm as Form
from wtforms import StringField
from wtforms.validators import DataRequired


class User(Form):
    username = StringField("useremail", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired])
    password_repeat = StringField("password1", validators=[DataRequired()])

class Books(Form):
    name = StringField("books", validators=[DataRequired()])