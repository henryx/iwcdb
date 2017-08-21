# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see LICENSE for details)
"""
import configparser
import io
import json

import bottle
import sys

__author__ = 'enrico'

__all__ = ["database", "validators"]


def read_json() -> dict:
    if bottle.request.body == "":
        raise bottle.HTTPError(status=500, body='No data received')

    try:
        data = io.TextIOWrapper(bottle.request.body)
        entity = json.load(data)
    except Exception as e:
        raise bottle.HTTPError(status=500, body=str("Malformed JSON"))

    return entity


def load_cfg():
    cfg = configparser.ConfigParser()
    try:
        cfg.read(sys.argv[1])
    except:
        print("Usage: " + sys.argv[0] + " <configfile>")
        sys.exit(1)

    return cfg
