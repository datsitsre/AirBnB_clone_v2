#!/usr/bin/python3
# Flask applications to listen on port 50000
""" Flask app Number template """

from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    ''' Print HTML Page'''
    return render_template('/5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    ''' Print HTML Page'''
    return render_template('/6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
