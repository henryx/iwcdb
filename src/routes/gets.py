# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see GPL.txt for details)
"""
import json
from configparser import ConfigParser

import bottle


class Gets:
    _cfg = None

    @property
    def cfg(self):
        return self._cfg

    def __init__(self, cfg: ConfigParser):
        self._cfg = cfg

    def index(self):
        return bottle.template("index", title="the Italian Web Comics Database")

    def serie(self):
        bottle.response.headers['Content-type'] = 'application/json'
        req = bottle.request.query.name or None

        if not req:
            bottle.response.status = 500
            return json.dumps({"result": "ko", "message": "no serie passed"})