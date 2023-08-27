from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function

@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def home():
    return "Helo World"

@app.route("/bye")

def say_bye():
    return "Bye"

@app.route("/<name>")
def greet(name):
    return f"Hello {name + 12}!"

if __name__ == "__main__":
    app.run(debug=True)



