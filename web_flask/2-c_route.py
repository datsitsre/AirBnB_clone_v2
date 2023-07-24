#!/usr/bin/python3
# Flask applications to listen on port 50000
""" Flask app to return a formated word """

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
