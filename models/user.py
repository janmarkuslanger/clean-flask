#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
