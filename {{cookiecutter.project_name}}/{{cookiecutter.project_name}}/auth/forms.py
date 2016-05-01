# -*- coding: utf-8 -*-

from {{cookiecutter.project_name}}.auth.documents import User


class LoginForm(object):

    def __init__(self, request):
        self.request = request
        self.data = request.form
        self.error = ''

    def save(self):

        if self.request.method == 'GET':
            return False

        data = self.data

        if 'username' not in data or 'password' not in data:
            self.error = 'You must fill the username and password'
            return False

        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            self.error = 'This user does not exist!'
            return False

        if user.verify_password(data['password']):
            return user
        else:
            self.error = 'Wrong password or username, try again!'
            return False
