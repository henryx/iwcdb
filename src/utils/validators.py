# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see LICENSE for details)
"""

import datetime

__author__ = 'enrico'


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
