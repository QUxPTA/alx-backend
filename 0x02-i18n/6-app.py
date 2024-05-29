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

    Priority:
    1. Locale from URL parameters.
    2. Locale from user settings.
    3. Locale from request header.
    4. Default locale.
    """
    # 1. Locale from URL parameters
    if 'locale' in request.args:
        requested_locale = request.args['locale']
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale

    # 2. Locale from user settings
    user = getattr(g, 'user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user['locale']

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Retrieve a user dictionary by ID.

    Returns:
        dict: The user dictionary or None.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Set the user as a global on flask.g before each request.
    """
    g.user = get_user()


@app.route('/')
def index():
    """
    Render the index.html template for the root route.

    Returns:
        str: Rendered HTML of the index.html template.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
