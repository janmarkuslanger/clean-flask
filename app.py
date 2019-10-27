#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import (
    Flask,
    render_template)
from controller.login import login_blueprint

app = Flask(__name__)

app.register_blueprint(login_blueprint)

@app.route('/')
def hello():
    return render_template('home.html')

if __name__ == '__main__':
    app.secret_key = 'My Key'
    app.run(debug=True)
