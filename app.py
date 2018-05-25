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

        # test book object
        book1 = Book()
        book1.title = 'SPRZEDAM OPLA'
        db.session.add(book1)

#add tile
        books_properties = get_book_data()
        book = Book()
        authors = Author()

        for elem in books_properties:
            title = elem['title']
        #    asset = elem['asset']
        #    title = book['title']
            book = Book(title = title)
        #    book.title = title

            authors = elem['authors']
            #print(type(authors))

            #under construction:
            # TODO: HANDLE WITH DIFFERENT TYPES OF AUTHORS
            '''for i in authors:
                type_i = type(i)
                if type_i is str:
                    print(i, 'string!')
                elif type_i is tuple:
                    f_name = i[0]
                    l_name = i[1]
                    author = Author(first_name = f_name, last_name = l_name)
                    print(i, 'tuple!', author)
                    db.session.add(author)
                else: # for list of authors
                    for elem in i:
                        print(i, 'list!')'''
                #print(f_name, l_name)
                    #db.session.add(author)
                #else:
                #    pass
            db.session.add(book)
        db.session.commit()
        print(Book.query.all()) #shows elements added to the database

    return app

create_app(DevConfig)

