# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see GPL.txt for details)
"""
from utils import database

__author__ = 'enrico'

__all__ = ["gets", "posts"]


class Routes:
    _db = None

    @property
    def db(self):
        return self._db

    def __init__(self, db: database.Database):
        self._db = db
