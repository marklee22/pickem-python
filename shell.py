#!/usr/bin/env python
# File to start an interactive console with flask server

__author__ = 'mlee'

import os
import readline
from pprint import pprint

from flask import *
from app import *

os.environ['PYTHONINSPECT'] = 'True'


