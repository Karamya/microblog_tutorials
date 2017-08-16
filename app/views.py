# @Author: karthick
# @Date:   2017-08-14T11:39:18+02:00
# @Last modified by:   karthick
# @Last modified time: 2017-08-14T12:38:58+02:00


#the script simply imports the app variable from our app package
# and invokes its run method to start hte server

from flask import render_template
from app import app  # imports app variable from the app package. See the file __init__.py

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)