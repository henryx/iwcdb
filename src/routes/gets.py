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
            bottle.response.status = 500
            return json.dumps({"result": "ko", "message": "no serie passed"})

        try:
            res = database.is_serie_exist(self.cfg, req)

            if res:
                # TODO: return serie JSON
                pass
        except _mysql_exceptions.OperationalError as e:
            bottle.response.status = 500
            return "Cannot connect to database"
