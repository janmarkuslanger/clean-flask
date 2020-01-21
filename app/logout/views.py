#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Blueprint,
    url_for,
    session,
    redirect
)

mod = Blueprint('logout', __name__)


@mod.route('/logout', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        del session['username']
    return redirect(url_for('login.index'))
