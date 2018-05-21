from app import db


class Book(db.Model):

    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(128), unique=True)
    authors = db.relationship('Author',
                              secondary='books_authors',
                              lazy='joined',
                              backref=db.backref('books'))
    title = db.Column(db.String(256))
    original_title = db.Column(db.String(256))
    table_of_contents = db.Column(db.String(256))
    publisher = db.Column(db.String(256))
    pub_date = db.Column(db.String(32))
    language = db.Column(db.String(56))
    tags = db.relationship('Tag',
                           secondary='books_tags',
                           lazy='subquery',
                           backref=db.backref('books'))
    description = db.Column(db.Text)
    copies = db.relationship('Copy',
                             backref=db.backref('book', uselist=False),
                             lazy='select',
                             cascade='all, delete-orphan')

    def __init__(self, **kwargs):
        super(Book, self).__init__(**kwargs)

    def __str__(self):
        return "'{}' by {}".format(
            self.title,
            ', '.join([str(a) for a in self.authors])
        )

    def __repr__(self):
        return "<Book: '{}' tags={} authors={} copies={}>".format(
            self.title,
            self.tags,
            self.authors,
            self.copies
        )


class Copy(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    asset_code = db.Column(db.Integer, unique=True)
    book_id = db.Column(db.Integer,
                        db.ForeignKey('books.id'),
                        nullable=False)
    # book = db.relationship('Book', foreign_keys=book_id, backref=db.backref(
    #     'copies', lazy='select', cascade='all, delete-orphan'))
    shelf = db.Column(db.String(56))
    cd_disk = db.Column(db.Boolean)
    rental_logs = db.relationship('RentalLog',
                                  backref=db.backref('copy'),
                                  lazy='dynamic',
                                  cascade='all, delete-orphan')

    def __repr__(self):
        return "<Copy: {} book_id={}>".format(self.asset_code, self.book_id)


class Author(db.Model):

    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __repr__(self):
        return "<Author: {} {}>".format(self.first_name, self.last_name)


class Tag(db.Model):

    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return "<Tag: {}>".format(self.name)


book_tag = db.Table('books_tags',
                    db.Column('book_id',
                              db.Integer,
                              db.ForeignKey('books.id')),
                    db.Column('tag_id',
                              db.Integer,
                              db.ForeignKey('tags.id')))

book_author = db.Table('books_authors',
                       db.Column('author_id',
                                 db.Integer,
                                 db.ForeignKey('authors.id')),
                       db.Column('book_id',
                                 db.Integer,
                                 db.ForeignKey('books.id')))