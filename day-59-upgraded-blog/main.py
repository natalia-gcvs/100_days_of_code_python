import smtplib
from flask import Flask, render_template, request
import requests
import os

blog_posts = requests.get(" https://api.npoint.io/86fc534f7c8af89e9eb8").json()['posts']

def send_email(name, email, phone, message):
    smtp_username = os.environ['smtp_email']
    smtp_password = os.environ['smtp_email_password']
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=smtp_username, password=smtp_password)
        connection.sendmail(from_addr=smtp_username, to_addrs='nagair.goncalves@gmail.com',
                            msg=f'Subject: Contact me\n\n{name}\n{email}\n{phone}\n{message}')

app = Flask(__name__)

@app.route("/")
def home():
    global blog_posts
    return render_template("index.html", posts=blog_posts)

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def get_contact():
    if request.method == "POST":
        data = request.form
        send_email(data['name'], data['email'], data['phone'], data['message'])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:id>")
def get_post(id):
    global blog_posts
    post_id = id
    return render_template("post.html", id_=post_id, posts=blog_posts)



if __name__ == "__main__":
    app.run(debug=True)

