#!/usr/bin/python3
'''A simple Flask web application.
'''

from flask import Flask

app = Flask(__name__)
"""Flask Apllication instance"""
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def ctext(text):
    return f'C {text.replace("_", " ")}'


@app.route('/python/')
@app.route('/python/<text>')
def pythontext(text='is_cool'):
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
