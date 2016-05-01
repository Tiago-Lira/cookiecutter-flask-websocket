# -*- coding: utf-8 -*-

from {{cookiecutter.project_name}}.tools import socketio
from {{cookiecutter.project_name}}.auth.decorators import authenticated_only
from {{cookiecutter.project_name}}.core.schemas import ExampleSchema


@socketio.listen('enter project')
@authenticated_only
def enter_project(data):
    socketio.join_room(data['project'])


@socketio.listen('leave project')
@authenticated_only
def leave_project(data):
    socketio.leave_room(data['project'])


@socketio.listen('list example')
@authenticated_only
def list_example(data):
    schema = ExampleSchema(many=True)
    queryset = schema.query()
    return schema.dump(queryset).data
