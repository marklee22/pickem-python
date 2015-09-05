# Configuration file for all the app settings

import os

__author__ = 'mlee'

_basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://pickem:password@localhost/pickem?charset=utf8'
SQLALCHEMY_ECHO = True