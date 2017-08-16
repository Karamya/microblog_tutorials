# @Author: karthick
# @Date:   2017-08-14T11:37:38+02:00
# @Last modified by:   karthick
# @Last modified time: 2017-08-14T12:52:02+02:00

from flask import Flask

app = Flask(__name__)    # app variable 
#app.config.from_object('config')

from app import views # app package
