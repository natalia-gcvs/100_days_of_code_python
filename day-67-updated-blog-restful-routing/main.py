from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime
from flask_htmlmin import HTMLMIN
import secrets



app = Flask(__name__)

app.config['HTML_MINIFY'] = True
htmlmin = HTMLMIN(app)

app.config['SECRET_KEY'] = secrets.token_hex(16)

ckeditor = CKEditor(app)

Bootstrap(app)


##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")



@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    post = BlogPost.query.get(post_id)
    if post:
        requested_post = BlogPost.query.filter_by(id=post_id).first()
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    requested_post = BlogPost.query.filter_by(id=post_id).first()
    data = {'title': requested_post.title, 'subtitle': requested_post.subtitle, 'author': requested_post.author,
            'img_url': requested_post.img_url, 'body': requested_post.body}
    form = CreatePostForm(data=data)
    if form.validate_on_submit():
        data = form.data
        post_to_update = BlogPost.query.get(post_id)
        post_to_update.title = data['title']
        post_to_update.subtitle = data['subtitle']
        post_to_update.author = data['author']
        post_to_update.img_url = data['img_url']
        post_to_update.body = data['body']
        post_to_update.date = datetime.now().strftime('%B %d, %Y')
        db.session.commit()
        return redirect(url_for('show_post', post_id=requested_post.id))
    return render_template("make-post.html", form=form)

@app.route("/new-post", methods=['GET','POST'])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        data = form.data
        new_post = BlogPost(title=data['title'], subtitle=data['subtitle'], author=data['author'],
                            img_url=data['img_url'], body=data['body'])
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)

@app.route("/delete/<post_id>")
def delete(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run()