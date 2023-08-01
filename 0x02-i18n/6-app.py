#!/usr/bin/env python3
'''Task 1's module.
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''Config class.'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    '''Get user from users dict.'''
    try:
        return users[int(request.args.get('login_as'))]
    except Exception:
        return None


@app.before_request
def before_request():
    '''Get user from request.'''
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale() -> str:
    '''Get locale from request.'''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user['locale']
        if locale and locale in app.config['LANGUAGES']:
            return locale

    headers = request.headers.get('Accept-Language')
    if headers:
        return headers.split(',')[0]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    '''Basic Flask app.'''
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
