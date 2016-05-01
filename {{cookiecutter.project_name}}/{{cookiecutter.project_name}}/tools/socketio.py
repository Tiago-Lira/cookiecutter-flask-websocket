# -*- coding: utf-8 -*-

import functools

from flask.ext.socketio import join_room as flask_join_room
from flask.ext.socketio import leave_room as flask_leave_room

from {{cookiecutter.project_name}}.application import socketio
from {{cookiecutter.project_name}}.auth.decorators import authenticated_only
from {{cookiecutter.project_name}}.exceptions import WebSocketError


namespace = functools.partial(socketio.on, namespace='/')


def emit(event, data, use_socket=True, **kwargs):
    if use_socket:
        return socketio.emit(event, data, **kwargs)
    else:
        return data


def listen(channel):
    def decorator(fn):
        @namespace(channel)
        @authenticated_only
        def wrapper(data):
            try:
                data = fn(data)
                return {'data': data, 'error': False}
            except WebSocketError as e:
                return {'data': {'message': e.message}, 'error': True}
        return wrapper
    return decorator


def join_room(name):
    return flask_join_room(name)


def leave_room(name):
    return flask_leave_room(name)
