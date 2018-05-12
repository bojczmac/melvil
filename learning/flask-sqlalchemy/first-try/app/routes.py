from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/all-books')
def all_books():
    return render_template('all-books.html')

@app.route('/search')
def search():
    return render_template('search.html')