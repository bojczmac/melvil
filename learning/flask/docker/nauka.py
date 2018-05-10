from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/user/<username>')
def hello(username):
    return 'hello %s' % username

@app.route('/d')
def num():
        return 'number'