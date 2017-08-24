# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see LICENSE for details)
"""

from configparser import ConfigParser
from contextlib import closing
import MySQLdb

__author__ = 'enrico'


class Database:
    _connection = None

    def __init__(self, cfg: ConfigParser):
        self._connection = MySQLdb.connect(host=cfg["database"]["host"],
                                           port=cfg.getint("database", "port"),
                                           database=cfg["database"]["database"],
                                           user=cfg["database"]["user"],
                                           password=cfg["database"]["password"])

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self._connection:
                self._connection.commit()
                self._connection.close()
        except:
            pass

    @property
    def connection(self):
        return self._connection


def is_serie_exist(cfg: ConfigParser, nome_serie: str) -> bool:
    query = "SELECT Count(*) FROM lk_serie WHERE nome_serie = %s"

    with Database(cfg) as db:
        with closing(db.connection.cursor()) as cursor:
            cursor.execute(query, (nome_serie,))

            value = cursor.fetchone()[0]

            if value > 0:
                return True
            else:
                return False


def add_albi(cfg: ConfigParser, data: dict) -> dict:
    # TODO: add valuta

    insert = " ".join(["INSERT INTO ft_albo(numero_albo,",
                       "nome_serie, data_uscita, prezzo)",
                       "VALUES(%(numero)s, %(serie)s, %(uscita)s, %(prezzo)s)"])

    if is_serie_exist(cfg, data["serie"]):
        with Database(cfg) as db:
            with closing(db.connection.cursor()) as cursor:
                cursor.execute(insert, data)

        return {"result": "ok", "message": "albo inserted"}
    else:
        return {"result": "ko", "message": "serie does not exist"}
