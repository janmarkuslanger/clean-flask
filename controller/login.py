#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    session
)
from models.user import User
from database import session as db_session

login_blueprint = Blueprint('login', __name__)


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = db_session.query(User).filter_by(
            username=request.form['username'],
            password=request.form['password']).one_or_none()

        if user:
            session['username'] = user.username
            return redirect(url_for('hello'))


    return render_template('login.html')
