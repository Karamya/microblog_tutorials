# @Author: karthick
# @Date:   2017-08-14T12:26:46+02:00
# @Last modified by:   karthick
# @Last modified time: 2017-08-14T12:52:21+02:00

from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
