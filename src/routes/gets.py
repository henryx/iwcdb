# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see GPL.txt for details)
"""
import bottle


def index():
    return bottle.template("index", title="the Italian Web Comics Database")


def serie():
    bottle.response.headers['Content-type'] = 'application/json'
    req = bottle.request.query.serie or None

