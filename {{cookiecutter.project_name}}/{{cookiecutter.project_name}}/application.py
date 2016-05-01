# -*- coding: utf-8 -*-

from os import path
from os import environ

from flask import Flask
from flask import render_template
from flask.ext.login import LoginManager
from flask.ext.compress import Compress
from flask.ext.mongoengine import MongoEngine
from flask.ext.socketio import SocketIO
from celery import Celery
from attrdict import AttrDict


__all__ = [
    'app',
    'settings',
    'db',
]


BASE_DIR = path.dirname(path.abspath(__file__))

TEMPLATE_DIR = path.join(path.dirname(BASE_DIR), 'frontend/templates')

STATIC_DIR = path.join(path.dirname(BASE_DIR), 'frontend/vendor')

ENVIRON = environ.get('CONFIG_ENVIRON', 'development')

CONFIG_PATH = '../environ/{}.cfg'.format(ENVIRON)

# Flask settings
app = Flask(
    __name__,
    static_url_path='/static',
    static_folder=STATIC_DIR,
    template_folder=TEMPLATE_DIR)
app.config.from_pyfile(CONFIG_PATH)

# Settings to be accessed by the modules
settings = AttrDict(app.config)

# GZip settings
Compress(app)

# Mongo engine config
db = MongoEngine(app)


# Login settings
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'

# Celery config
if 'BROKER_URL' not in settings:
    celery = Celery(__name__, backend='amqp', broker=settings.BROKER_URL)
    celery.conf.add_defaults(app.config)

# Socket.IO Settings
socketio = SocketIO(
    app=app,
    async_mode='eventlet',
    message_queue=settings.BROKER_URL)


@app.route('/')
@app.route('/<path:path>')
def index(path=None):
    """Serve the client-side application."""
    return render_template('index.html')
