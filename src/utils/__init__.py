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

__author__ = 'enrico'

__all__ = ["database", "json"]


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
