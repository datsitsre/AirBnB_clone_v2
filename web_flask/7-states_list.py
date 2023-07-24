#!/usr/bin/python3
# Flask applications to listen on port 50000
""" Flask app Number template """
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    '''Print State Page'''
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    ctxt = {
        'states': all_states
    }
    return render_template('7-states_list.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    ''' The flask request ''' 
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
