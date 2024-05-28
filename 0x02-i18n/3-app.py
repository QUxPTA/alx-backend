#!/usr/bin/env python3
"""
Parametrizing templates
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
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
