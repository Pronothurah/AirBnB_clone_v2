#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask, render_template

from models import storage
from models.amenity import Amenity
from models.state import State


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def hbnb_filters():
    """Display content from html files for the route"""
    all_states = storage.all(cls=State)
    all_amenities = storage.all(cls=Amenity)

    return render_template(
        "10-hbnb_filters.html", states=all_states, amenities=all_amenities
    )



@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
