from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)

from flask import url_for

@app.route('/')
def index():
    return 'index'

# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'



