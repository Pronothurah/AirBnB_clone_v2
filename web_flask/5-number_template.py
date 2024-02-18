#!/usr/bin/python3
'''A simple Flask web application.
'''

from flask import Flask, render_template

app = Flask(__name__)
"""Flask Apllication instance"""
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Base route"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """hbnb route"""
    return 'HBNB'


@app.route('/c/<text>')
def ctext(text):
    """Display text (C + @text)"""
    return f'C {text.replace("_", " ")}'


@app.route('/python/')
@app.route('/python/<text>')
def pythontext(text='is_cool'):
    """Display text (Python + @text)"""
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>')
def number(n):
    """Display text (@n + is a number)"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Display content from html files for the route"""
    return render_template('5-number.html', number = n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
