#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Blueprint,
    request,
    url_for,
    session,
    redirect
)
from models.user import User
from database import session as db_session

logout_blueprint = Blueprint('logout', __name__)


@logout_blueprint.route('/logout', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        del session['username']
        return redirect(url_for('login.login'))
