#!/usr/bin/python3
"""
a script that starts a Flask web application:
listens on 0.0.0.0, port 5000
Routes:	/: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C” followed by the value of text
    displays “Python ”, followed by the value of the text
    displays “n is a number” only if n is an integer
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """function for web app route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """displays /hbnb web app route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """dispalys the value of /c/<text>"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route("/python", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python_route(text="is cool"):
    """displays the value of /python/<text>"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """displays /number/<n> web app route"""
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
