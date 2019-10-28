#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from database import create_db, session
from models.user import User

create_db()

# Create a demo user
user = User(name='Demo', username='demo')
user.hash_password('demo')
try:
    session.add(user)
    session.commit()
except Exception as e:
    print(e)
    session.rollback()
