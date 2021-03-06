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


def is_serie_exist(db: Database, nome_serie: str) -> bool:
    query = "SELECT Count(*) FROM lk_serie WHERE nome_serie = %s"

    with closing(db.connection.cursor()) as cursor:
        cursor.execute(query, (nome_serie,))

        value = cursor.fetchone()[0]

        if value > 0:
            return True
        else:
            return False


def is_collana_exists(db: Database, nome_collana: str, nome_editore: str):
    query = "SELECT Count(*) FROM lk_collana WHERE nome_collana = %s AND nome_editore = %s"

    with closing(db.connection.cursor()) as cursor:
        cursor.execute(query, (nome_collana, nome_editore))

        value = cursor.fetchone()[0]

        if value > 0:
            return True
        else:
            return False


def add_albi(db: Database, data: dict) -> dict:
    # TODO: add valuta

    insert = " ".join(["INSERT INTO ft_albo(numero_albo,",
                       "nome_serie, data_uscita, prezzo)",
                       "VALUES(%(numero)s, %(serie)s, %(uscita)s, %(prezzo)s)"])

    if is_serie_exist(db, data["serie"]):
        with closing(db.connection.cursor()) as cursor:
            cursor.execute(insert, data)

        return {"result": "ok", "message": "albo inserted"}
    else:
        return {"result": "ko", "message": "serie does not exist"}


def add_collana(db: Database, data: dict) -> dict:
    # TODO: add collana
    return {"result": "ok", "message": "collana inserted"}


def get_editore(db: Database, name: str = None, limit: int = None, offset: int = None) -> dict:
    res = {
        "data": [],
        "result": "ko",
        "size": 0
    }
    filters = []

    query = "SELECT nome_editore, sede_editore FROM lk_editore"
    if name:
        query = query + "WHERE nome_editore = %s"
        filters.append(name)
    if limit:
        query = query + " LIMIT %s"
        filters.append(limit)
        if offset:
            query = query + ",%s"
            filters.append(offset)

    with closing(db.connection.cursor()) as cursor:
        if len(filters) == 0:
            cursor.execute(query)
        else:
            cursor.execute(query, filters)

        for row in cursor:
            data = {
                "nome": row[0],
                "sede": row[1]
            }

            res["data"].append(data)
            res["size"] += 1

        if res["size"] > 0:
            res["result"] = "ok"

    return res
