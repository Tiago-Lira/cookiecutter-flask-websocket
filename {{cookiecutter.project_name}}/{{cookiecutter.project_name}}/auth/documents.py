# -*- coding: utf-8 -*-

from {{cookiecutter.project_name}}.application import db
from passlib.apps import custom_app_context as pwd_context


class User(db.Document):
    username = db.StringField(unique=True)
    password_hash = db.StringField()
    token = db.StringField(unique=True)
    logged_at = db.DateTimeField()
    is_active = db.BooleanField(default=True)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def get_id(self):
        return str(self.id)
