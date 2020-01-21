#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    session,
    redirect
)
from app import db
from app.user.models import User

mod = Blueprint('login', __name__, url_prefix='/login')


@mod.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = db.session.query(User).filter_by(
            username=request.form['username']).one_or_none()

        if user and user.verify_password(request.form['password']):
            session['username'] = user.username
            return redirect(url_for('dashboard.index'))


    return render_template('/login/index.html')
