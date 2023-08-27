# MINIMAL FLASK APPLICATION

# First we imported the Flask class. An instance of this class will be our WSGI application.
from flask import Flask
# Next we create an instance of this class. The first argument is the name of the application’s module or package.
# __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows
# where to look for resources such as templates and static files.
app = Flask(__name__)

# We then use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
# The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML
# in the string will be rendered by the browser.
def hello_world():
    return 'Hello World!'

# To run the application, use the flask command or python -m flask. You need to tell the Flask where your application is
# with the --app option.

#$ flask --app hello run
# that tells flask what the name of the file that contains our server
 # * Serving Flask app 'hello'
 # * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

# this save us from having to type set FLASK_APP=hello.py in the terminal
if __name__ == "__main__":
    app.run()

# EXAMPLE OF NESTED FUNCTION

def outer_function():
    print("test 1")

    def inner_function():
        print("test 2")

    return inner_function

nested_function = outer_function()
nested_function()

# DEMONSTRATION OF DECORATOR FUNCTION

import time

def decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after
        time.sleep(2)
    return wrapper_function


@decorator_function
def say_hello():
    print('Hello')





















