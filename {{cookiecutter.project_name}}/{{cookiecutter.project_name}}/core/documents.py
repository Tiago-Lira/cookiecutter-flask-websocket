# -*- coding: utf-8 -*-

from {{cookiecutter.project_name}}.application import db


class Example(db.Document):
    name = db.StringField()
