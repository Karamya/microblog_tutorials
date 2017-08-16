# @Author: karthick
# @Date:   2017-08-14T12:23:27+02:00
# @Last modified by:   karthick
# @Last modified time: 2017-08-14T12:51:18+02:00

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess' # secret key setting is necessary
                                    # only when CSRF is enabled

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
