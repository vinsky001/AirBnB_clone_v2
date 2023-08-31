#!/usr/bin/python3
""" flask script """

from flask import Flask


app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_route():
    """Returns a string route"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
