from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)

@app.route('/')
def home():
    all_blog_posts = requests.get(" https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=all_blog_posts )

@app.route("/post/<int:id>")
def get_post(id):
    post = Post(id).get_post()
    full_post = {'id': post["id"], 'title': post["title"], 'subtitle': post["subtitle"], 'body': post["body"]}
    return render_template("post.html", post_=full_post)

if __name__ == "__main__":
    app.run(debug=True)
