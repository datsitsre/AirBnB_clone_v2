#!/usr/bin/python3
# Flask applications to listen on port 50000

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb_hello():
    ''' print hello HBNB '''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
