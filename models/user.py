#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from database import Base
from passlib.apps import custom_app_context as pwd_context


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String(80), nullable=False)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
