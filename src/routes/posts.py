# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see GPL.txt for details)
"""
import json

import bottle

import utils
from routes import Routes


class Posts(Routes):
    def __init__(self, db: utils.database.Database):
        super(Posts, self).__init__(db)

    def albi(self):
        bottle.response.headers['Content-type'] = 'application/json'
        fields = [
            "serie",
            "numero",
            "uscita",
            "prezzo"
        ]

        entity = utils.read_json()
        try:
            if utils.validate_structure(entity, fields, ["uscita", ]):
                result = utils.database.add_albi(self.db, entity)
                if result["result"] == "ok":
                    return json.dumps(result)
                else:
                    raise Exception(result["message"])
        except Exception as e:
            raise bottle.HTTPError(status=500, body=str(e))

    def serie(self):
        bottle.response.headers['Content-type'] = 'application/json'

        entity = utils.read_json()
        # TODO: insert serie into database

    def collana(self):
        bottle.response.headers['Content-type'] = 'application/json'
        fields = [
            "nome",
            "editore"
        ]

        entity = utils.read_json()
        try:
            if utils.validate_structure(entity, fields):
                # TODO: add collana
                pass
        except Exception as e:
            raise bottle.HTTPError(status=500, body=str(e))