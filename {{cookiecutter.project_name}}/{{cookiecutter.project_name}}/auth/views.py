# # -*- coding: utf-8 -*-

from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import jsonify
from flask.ext.login import login_user
from flask.ext.login import logout_user

from {{cookiecutter.project_name}}.auth.documents import User
from {{cookiecutter.project_name}}.auth.forms import LoginForm
from {{cookiecutter.project_name}}.application import app
from {{cookiecutter.project_name}}.application import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.objects.get(id=user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Authenticate the user with the provided credentials

    The argument "data" must have the keys "username" and "password"
    to authenticate the user. If the credentials are correct, then a
    token will be generated from the "password" and "getconfig()".

    If the credentials are wrong, this method will raise an exception
    to the client.
    """
    form = LoginForm(request)
    user = form.save()
    if user:
        login_user(user, remember=True)
        next = request.args.get('next')
        return redirect(next or url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({
        'message': 'logged out with success',
    })
