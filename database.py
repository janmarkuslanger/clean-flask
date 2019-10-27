#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Connect to database and create database session.
engine = create_engine("sqlite:///app.db",connect_args={'check_same_thread': False})
Base = declarative_base()
DBSession = sessionmaker(bind=engine)
session = DBSession()


def create_db():
    Base.metadata.create_all(engine)
