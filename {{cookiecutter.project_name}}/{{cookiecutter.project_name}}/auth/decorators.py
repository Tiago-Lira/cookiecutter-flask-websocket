# -*- coding: utf-8 -*-

import functools

from flask.ext.login import current_user
from flask.ext.socketio import disconnect


def authenticated_only(fn):
    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return fn(*args, **kwargs)
    return wrapped
