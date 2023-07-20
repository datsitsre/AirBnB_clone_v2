#!/usr/bin/python3
# Flask applications to listen on port 50000

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb_hello():
    ''' print hello HBNB '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' print HBNB '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    ''' Print C with a text'''
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    ''' Print Python with a text'''
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    ''' Print N with a text'''
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
