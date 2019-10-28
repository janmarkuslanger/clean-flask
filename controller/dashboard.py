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
from models.user import User
from database import session as db_session
from core.auth import login_required

dashboard_blueprint = Blueprint('dashboard', __name__)


@dashboard_blueprint.route('/dashboard')
@login_required
def index():
    return render_template('dashboard.html', username=session['username'])
