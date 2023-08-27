import time

def decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        result = function()
        # Do something after
        time.sleep(2)
        return result
    return wrapper_function

@decorator_function
def say_hello():
    return "Hello"
