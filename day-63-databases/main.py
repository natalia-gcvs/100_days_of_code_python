from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():

    # creates database
    # db.create_all()

    # # alters a column name
    # db.session.execute(text('ALTER TABLE books RENAME COLUMN name TO title;'))
    # db.session.commit()

    # creates a new record
    book = Books(title='It', author='Stephen King', rating=5)
    db.session.add(book)
    db.session.commit()

    # reads all records
    all_books = db.session.query(Books).all()

    print(type(all_books), all_books[0:4])

    # #read a particular record by query
    # book = Books.query.filter_by(title='The Alchemist').first()

    #update a particular record by query
    # book_to_update = Books.query.filter_by(title='The Alchemist').first()
    # book_to_update.title = 'The Alchemist I'
    # db.session.commit()

    # #update a record by primary key
    # book_id = 1
    # book_to_update = Books.query.get(book_id)
    # book_to_update.title = 'The Alchemist'
    # db.session.commit()
    #
    # #delete a particular record by primary key
    # book_id = 1
    # book_to_delete = Books.query.get(book_id)
    # db.session.delete(book_to_delete)
    # db.session.commit()



    print(book)

