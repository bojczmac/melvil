from flask import Flask
from views import library
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from xlsx_reader import get_book_data
db = SQLAlchemy()

def create_app(config=DevConfig):

    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(library)

    db.init_app(app)

    from models import (Book, Author)
    with app.app_context():
        db.create_all()

        books_properties = get_book_data()

        for elem in books_properties:
            title = elem['title']
            asset = elem['asset']
        #   title = book['title']
        #    book = Book(title = title)
        #   book.title = title
            authors = elem['authors']
            book_authors = []
            if type(authors) is tuple:
                f_name = str(authors[0])
                l_name = str(authors[1])
                author = Author(first_name=f_name, last_name=l_name)
                book_authors.append(author)
                #print(f_name, l_name)
                db.session.add(author)
            elif type(authors) is list:
                for i in authors:
                    f_name = str(i[0])
                    l_name = str(i[1])
                    author = Author(first_name = f_name, last_name = l_name)
                    #print(authors, i, 'list!', author)
                    db.session.add(author)
                    book_authors.append(author)
            else:
                #author = None # for list of authors
                #print(authors, 'other type!', type(authors), author)
                book_authors = []
            book = Book(title = title, authors = book_authors) # TODO: add asset_code = asset
        db.session.add(book)
        db.session.commit()

        #print(db.session.query(Author).all())
        print(db.session.query(Book).all())
    return app

create_app(DevConfig)


