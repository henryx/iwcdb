# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see GPL.txt for details)
"""
import psycopg2

__author__ = 'enrico'


class Database:
    _connection = None

    def __init__(self, cfg):
        self._conn = psycopg2.connect(host=cfg["database"]["host"],
                                      port=cfg["database"]["port"],
                                      database=cfg["database"]["database"],
                                      user=cfg["database"]["user"],
                                      password=cfg["database"]["password"])

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self._conn:
                self._conn.commit()
                self._conn.close()
        except:
            pass

    @property
    def connection(self):
        return self._connection
