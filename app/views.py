# @Author: karthick
# @Date:   2017-08-14T11:39:18+02:00
# @Last modified by:   karthick
# @Last modified time: 2017-08-14T12:38:58+02:00


#the script simply imports the app variable from our app package
# and invokes its run method to start hte server
from flask import render_template
from app import app
from .forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
