#!/usr/bin/env python3
"""
Add users
"""
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _, format_datetime
import pytz
from pytz.exceptions import UnknownTimeZoneError

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


@babel.timezoneselector
def get_timezone():
    """
    Determine the best time zone.

    Priority:
    1. Timezone from URL parameters.
    2. Timezone from user settings.
    3. Default to UTC.
    """
    # 1. Timezone from URL parameters
    if 'timezone' in request.args:
        requested_timezone = request.args['timezone']
        try:
            return pytz.timezone(requested_timezone).zone
        except UnknownTimeZoneError:
            pass

    # 2. Timezone from user settings
    user = getattr(g, 'user', None)
    if user and user.get('timezone'):
        try:
            return pytz.timezone(user['timezone']).zone
        except UnknownTimeZoneError:
            pass

    # 3. Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


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


def get_current_time():
    """
    Get the current time in the appropriate time zone.

    Returns:
        str: The current time formatted as a string.
    """
    timezone = get_timezone()
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    return format_datetime(current_time)


@app.route('/')
def index():
    """
    Render the index.html template for the root route.

    Returns:
        str: Rendered HTML of the index.html template.
    """
    current_time = get_current_time()
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
