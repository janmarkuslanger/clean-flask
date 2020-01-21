#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Blueprint, render_template

mod = Blueprint('index', __name__)


@mod.route('/')
def index():
    return render_template('/home/index.html')
