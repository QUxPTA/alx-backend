#!/usr/bin/env python3
"""
Add users
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


app = Flask(__name__)


class Config:
    """Configuration class for Flask app with Babel settings."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """
    Determine the best match with our supported languages.

    Returns:
        str: The best match language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index.html template for the root route.

    Returns:
        str: Rendered HTML of the index.html template.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
