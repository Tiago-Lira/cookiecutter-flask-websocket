#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from {{cookiecutter.project_name}}.application import socketio
    from {{cookiecutter.project_name}}.application import app
    socketio.run(app, host='0.0.0.0', port=8000)
