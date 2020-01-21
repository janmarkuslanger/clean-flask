#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create app
app = Flask(__name__)
app.config.from_object('config')

# create db connection
db = SQLAlchemy(app)

# register blueprints
