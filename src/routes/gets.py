# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see GPL.txt for details)
"""
import json

import _mysql_exceptions
import bottle

from utils import database


class Gets:
    _db = None

    @property
    def db(self):
        return self._db

    def __init__(self, db: database.Database):
        self._db = db

    def index(self):
        return bottle.template("index", title="the Italian Web Comics Database")

    def serie(self):
        bottle.response.headers['Content-type'] = 'application/json'
        req = bottle.request.query.name or None

        if not req:
            raise bottle.HTTPError(status=500, body="no serie passed")

        try:
            res = database.is_serie_exist(self.db, req)

            if res:
                # TODO: return serie JSON
                pass
            else:
                raise bottle.HTTPError(status=500, body="Serie {} not exist".format(req))
        except _mysql_exceptions.OperationalError as e:
            bottle.response.status = 500
            raise bottle.HTTPError(status=500, body="Cannot connect to database")

