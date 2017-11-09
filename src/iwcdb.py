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
from routes import gets, posts

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

    with utils.database.Database(cfg) as db:
        g = gets.Gets(db)
        p = posts.Posts(db)

        app.route("/", method="GET", callback=g.index)
        app.route("/serie", method="GET", callback=g.serie)
        app.route("/serie/<name>", method="GET", callback=g.serie)
        app.route("/collana", method="GET", callback=g.collana)
        app.route("/collana/<name>", method="GET", callback=g.collana)
        app.route("/editore", method="GET", callback=g.editore)

        app.route("/serie", method="POST", callback=p.serie)
        app.route("/albi", method="POST", callback=p.albi)
        app.route("/collana", method="POST", callback=p.collana)

        bottle.run(app=app,
                   host=cfg["service"]["listen"],
                   port=int(cfg["service"]["port"]),
                   debug=cfg["service"].getboolean("debug"),
                   reloader=True)
