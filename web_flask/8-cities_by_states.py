#!/usr/bin/python3
"""
This module is about listing states from db
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)
"""Flask Apllication instance"""
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """Display content from html files for the route"""
    all_states = storage.all("State")
    return render_template("7-states_list.html", states=all_states)


@app.route("/cities_by_states")
def cities_by_states():
    all_states = storage.all("State")
    return render_template("8-cities_by_states.html", states=all_states)


@app.teardown_appcontext
def close_storage(exception):
    """Close sqlalchemy session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
