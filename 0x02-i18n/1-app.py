#!/usr/bin/python3
"""
A Config class that has a LANGUAGES class attribute
"""
from flask import Flask, render_template
from flask_babel import Babel
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration class for Flask app with Babel settings."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    Render the index.html template for the root route.

    Returns:
        str: Rendered HTML of the index.html template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
