from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
import secrets


app = Flask(__name__)

Bootstrap(app)
app.secret_key = secrets.token_urlsafe(16)

class CredentialsChecker:
    def __init__(self, credential="", message=None):
        self.credential = credential
        if not message:
            message = 'Incorrect credentials'
        self.message = message

    def __call__(self, form, field):
        l = field.data
        if l != self.credential:
            raise ValidationError(self.message)

credentials_checker = CredentialsChecker


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(), credentials_checker(credential='your_email')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8), credentials_checker(credential='your_password')])
    submit = SubmitField(label='Log in')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('success'))
        return redirect(url_for('denied'))
    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)