# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see GPL.txt for details)
"""

import configparser
import json
import bottle
import sys

__author__ = 'enrico'

app = application = bottle.Bottle()


def load_cfg():
    cfg = configparser.ConfigParser()
    try:
        cfg.read(sys.argv[1])
    except:
        print("Usage: " + sys.argv[0] + " <configfile>")
        sys.exit(1)

    return cfg


@app.hook('before_request')
def strip_path():
    bottle.request.environ['PATH_INFO'] = bottle.request.environ[
        'PATH_INFO'].rstrip('/')


@app.error(500)
def error500(error):
    return json.dumps({"result": "ko", "message": error.body})


@app.route("/albi", method="GET")
def albi():
    bottle.response.headers['Content-type'] = 'application/json'
    serie = bottle.request.query.serie or None


@app.route("/albi/add", method="POST")
def albi():
    bottle.response.headers['Content-type'] = 'application/json'


@app.route("/")
def index():
    return bottle.template("index", title="the Italian Web Comics Database")


if __name__ == "__main__":
    cfg = load_cfg()

    bottle.run(app=app,
               host=cfg["service"]["listen"],
               port=int(cfg["service"]["port"]),
               debug=cfg["service"].getboolean("debug"),
               reloader=True)
