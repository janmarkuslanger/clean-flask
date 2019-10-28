#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Flask,
    render_template)

from controller.login import login_blueprint
from controller.logout import logout_blueprint
from controller.dashboard import dashboard_blueprint


app = Flask(__name__)

app.register_blueprint(login_blueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(dashboard_blueprint)


@app.route('/')
def hello():
    return render_template('home.html')

if __name__ == '__main__':
    app.secret_key = 'My Key'
    app.run(debug=True)
