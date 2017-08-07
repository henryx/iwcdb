#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see GPL.txt for details)
"""

import configparser
import io
import json
import bottle
import sys
import utils.json
from utils import database

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


def read_json() -> dict:
    if bottle.request.body == "":
        raise bottle.HTTPError(status=500, body='No data received')

    try:
        data = io.TextIOWrapper(bottle.request.body)
        entity = json.load(data)
    except Exception as e:
        raise bottle.HTTPError(status=500, body=str("Malformed JSON"))

    return entity


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
    # TODO: return albi JSON


@app.route("/albi/add", method="PUT")
def albi():
    bottle.response.headers['Content-type'] = 'application/json'

    entity = read_json()
    try:
        if utils.json.validate_albi(entity):
            result = database.add_albi(load_cfg(), entity)
            if result["result"] == "ok":
                return json.dumps(result)
            else:
                raise Exception(result["message"])
    except Exception as e:
        raise bottle.HTTPError(status=500, body=str(e))


@app.route("/serie", method="GET")
def serie():
    bottle.response.headers['Content-type'] = 'application/json'
    serie = bottle.request.query.serie or None
    # TODO: return serie JSON


@app.route("/serie/add", method="PUT")
def serie():
    bottle.response.headers['Content-type'] = 'application/json'

    entity = read_json()
    # TODO: insert serie into database


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
