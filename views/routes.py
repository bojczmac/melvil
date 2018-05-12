from flask import render_template
from . import library


@library.route('/')
def index():
    return render_template('index.html')


@library.route('/all-books')
def all_books():
    return render_template('all-books.html')


@library.route('/search')
def search():
    return render_template('search.html')