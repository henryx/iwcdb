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

@app.route("/albi", method="GET")
def albi():
    pass

@app.route("/albi/add", method="POST")
def albi():
    pass

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
