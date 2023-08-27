from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().strftime('%Y')
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def predict(name):
    predicted_age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    predicted_gender = requests.get(f"https://api.genderize.io?name={name}").json()['gender']
    name = name.title()
    return render_template("guess.html", name=name, age=predicted_age, gender=predicted_gender)

@app.route("/blog")
def get_blog():
    blog_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)