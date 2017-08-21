#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see LICENSE for details)
"""

import json

import bottle

import utils
from routes import gets, puts

__author__ = 'enrico'

app = application = bottle.Bottle()


@app.hook('before_request')
def strip_path():
    bottle.request.environ['PATH_INFO'] = bottle.request.environ['PATH_INFO'].rstrip('/')


@app.error(500)
def error500(error):
    return json.dumps({"result": "ko", "message": error.body})


if __name__ == "__main__":
    cfg = utils.load_cfg()

    app.route("/", method="GET", callback=gets.index)
    app.route("/serie", method="GET", callback=gets.serie)

    app.route("/serie/add", method="PUT", callback=puts.serie)
    app.route("/albi/add", method="PUT", callback=puts.albi)

    bottle.run(app=app,
               host=cfg["service"]["listen"],
               port=int(cfg["service"]["port"]),
               debug=cfg["service"].getboolean("debug"),
               reloader=True)
