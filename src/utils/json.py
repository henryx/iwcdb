# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see GPL.txt for details)
"""
import datetime

__author__ = 'enrico'


def validate_albi(data: dict) -> bool:
    # TODO: check valuta
    fields = [
        "serie",
        "numero",
        "uscita",
        "prezzo"
    ]

    for field in fields:
        if field not in data:
            raise ValueError(field + " is missing in JSON")

    try:
        datetime.datetime.strptime(data["uscita"], '%Y-%m-%d')
    except:
        raise ValueError("Malformed date in JSON uscita field")

    return True
