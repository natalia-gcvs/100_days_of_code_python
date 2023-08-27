from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import secrets

app = Flask(__name__)

# Initialize the Flask-Login extension
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = secrets.token_hex(16)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

#Line below only required once, when creating DB. 
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email_already_exists = User.query.filter_by(email=request.form['email']).first()
        if email_already_exists:
            flash("You've already signed up with that email, log in instead")
            return redirect(url_for('login'))
        else:
            hashed_password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
            new_user = User(email=request.form['email'], name=request.form['name'],
                            password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            # Log in and authenticate user after adding details to database.
            login_user(new_user)
            return redirect(url_for('secrets'))

    return render_template("register.html")


# Define the login route and view function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        # Check stored password hash against entered password hashed.
        if check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash('Invalid email or password.')
    return render_template('login.html')


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/download')
def download():
    return send_from_directory('static', filename='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
