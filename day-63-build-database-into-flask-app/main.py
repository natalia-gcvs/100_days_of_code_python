from flask import Flask, render_template, request, redirect, url_for, current_app
#to generate a 16 characters secret key. We need this to be able to create a form
import secrets
# importing the bootstrap class to initialize it
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from custom_forms import BookForm, RatingUpdate


app = Flask(__name__)

app.secret_key = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initializing the extension by creating an instance of the Bootstrap class and passing your app as a parameter.
bootstrap = Bootstrap(app)
# initializing the extension by creating an instance of the SQLAlchemy class and passing your app as a parameter.
db = SQLAlchemy(app)

# creates a table in the database
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():

    # db.create_all()

    all_books = db.session.query(Books).all()

    @app.route('/')
    def home():
        #reads al entries in the database
        all_books = db.session.query(Books).all()
        return render_template('index.html', books=all_books)

    @app.route("/add", methods=['GET', 'POST'])
    def add():
        form = BookForm()
        if form.validate_on_submit():
            entry = form.data
            book = Books(title=entry['title'], author=entry['author'], rating=entry['rating'])
            db.session.add(book)
            db.session.commit()
            form = BookForm(formdata=None)
        return render_template('add.html', form=form)

    @app.route("/edit/<int:id>", methods=['GET', 'POST'])
    def edit(id):
        form = RatingUpdate()
        book_id = id
        if form.validate_on_submit():
            book_to_update = Books.query.get(book_id)
            book_to_update.rating = form.data['rating']
            db.session.commit()
            return(redirect(url_for('home')))
        return render_template('edit.html', form=form, id=book_id, books=all_books)

    @app.route("/delete")
    def delete():
        book_id = request.args.get('id')

        # DELETE A RECORD BY ID
        book_to_delete = Books.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))

    if __name__ == "__main__":
        app.run(debug=True)




