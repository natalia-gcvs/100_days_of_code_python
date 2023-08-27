from flask import Flask
from random import choice

app = Flask(__name__)

@app.route("/")
def hello():
    return f'<h1>Guess a number between 0 and 9</h1> ' \
           f'<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="" width="" height="">'

@app.route("/<int:guess>")
def number_guessed(guess):
    random_number = choice(range(9))
    print(random_number)
    if guess == random_number:
        return f'<h1 style="color:purple">You have guessed it"</h1> '\
               f'<img src="https://media.giphy.com/media/t0TNY68t8wq2Y/giphy.gif" alt="" width="" height="">'
    elif guess > random_number:
        return f'<h1 style="color:purple">Too high. Try again</h1> ' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="" width="" height="">'
    else:
        return f'<h1 style="color:blue">Too low. Try again</h1> ' \
               f'<img src="https://media.giphy.com/media/dYtt1opESBL3i/giphy.gif" alt="" width="" height="">'


if __name__ == "__main__":
    app.run(debug=True)