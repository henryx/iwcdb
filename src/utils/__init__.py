# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see LICENSE for details)
"""
import configparser
import datetime
import io
import json
import os
import sys

import bottle

from . import database

__author__ = 'enrico'

__all__ = ["database", ]


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
        if os.path.exists(sys.argv[1]):
            cfg.read(sys.argv[1])
        else:
            print("File {} not exitst".format(sys.argv[1]))
            raise FileNotFoundError
    except:
        print("Usage: " + sys.argv[0] + " <configfile>")
        sys.exit(1)

    return cfg


def validate_structure(data: dict, fields: list, date_fields: list = None) -> bool:
    for field in fields:
        if field not in data:
            raise ValueError(field + " is missing in JSON")

    if date_fields:
        for field in date_fields:
            try:
                datetime.datetime.strptime(data[field], '%Y-%m-%d')
            except:
                raise ValueError("Malformed date in JSON {} field".format(field))

    return True
