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


def validate_albi(data):
    if "id" not in data:
        raise ValueError("id is missing in JSON")

    if "serie" not in data:
        raise ValueError("serie is missing in JSON")

    if "numero" not in data:
        raise ValueError("numero is missing in JSON")

    if "uscita" not in data:
        raise ValueError("uscita is missing in JSON")
    else:
        try:
            datetime.datetime.strptime(data["uscita"], '%Y-%m-%d')
        except:
            raise ValueError("Malformed date in JSON uscita field")

    if "prezzo" not in data:
        raise ValueError("prezzo is missing in JSON")

    # TODO: check valuta

    return True
