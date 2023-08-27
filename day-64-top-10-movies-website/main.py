import secrets
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from custom_forms import UpdateRatingForm, AddMovieForm
import requests
import os

MOVIE_DB_API_KEY = os.environ.get('TMDB_API_KEY')
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_top-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

with app.app_context():
    db.create_all()

    @app.route("/", methods=['GET', 'POST'])
    def home():
        all_movies = db.session.query(Movie).order_by(Movie.rating).all()
        for index in range(len(all_movies)):
            # This line gives each movie a new ranking reversed from their order in all_movies
            all_movies[index].ranking = len(all_movies) - index
        db.session.commit()
        return render_template("index.html", movies=all_movies)

    @app.route("/add", methods=['GET', 'POST'])
    def add():
        add_form = AddMovieForm()
        if add_form.validate_on_submit():
            title = add_form.data['title']
            query = {
                'api_key': MOVIE_DB_API_KEY,
                'query': title,
            }
            response = requests.get(MOVIE_DB_SEARCH_URL, params=query)
            movie_data = response.json()['results']
            return render_template('select.html', movies=movie_data)
        return render_template('add.html', form=add_form)


    @app.route("/find")
    def find_movie():
        data = eval(request.args.get("id"))
        if data:
            new_movie = Movie(
                title=data["title"],
                year=data["release_date"].split("-")[0],
                img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
                description=data["overview"]
            )
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for("update", id=new_movie.id))


    @app.route("/update", methods=['GET', 'POST'])
    def update():
        update_form = UpdateRatingForm()
        movie_id = request.args.get('id')
        print(movie_id)
        movie_to_update = Movie.query.get(movie_id)
        if update_form.validate_on_submit():
            movie_to_update.review = update_form.data['review']
            movie_to_update.rating = update_form.data['rating']
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('edit.html', form=update_form)


    @app.route("/delete")
    def delete():
        movie_id = request.args.get('id')
        movie_to_delete = Movie.query.get(movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


    if __name__ == '__main__':
        app.run(debug=True)
