from flask_wtf import Form
from wtforms import TextField,PasswordField,TextAreaField
from wtforms.validators import Required
from wtforms.validators import ValidationError

from project.model.account import User


class LoginForm(Form):
    username = TextField('user',validators=[Required()])
    password = PasswordField('password',validators=[Required()])

class addForm(Form):
    title=TextField('title',validators=[Required()])
    content=TextAreaField('content')
