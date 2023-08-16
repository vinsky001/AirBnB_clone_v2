#!/usr/bin/python3
""" flask script """

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Returns a string route"""
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
