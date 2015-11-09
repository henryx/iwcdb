# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see GPL.txt for details)
"""

__author__ = 'enrico'


def validate_albi(data):
    if "id" not in data:
        raise ValueError("id is missing in JSON")

    return True
