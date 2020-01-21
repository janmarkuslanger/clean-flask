#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from app import db
from app.user.models import User

if __name__ == '__main__':
    db.create_all()
