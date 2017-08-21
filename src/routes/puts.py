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
import utils.database
import utils.validators


def albi():
    bottle.response.headers['Content-type'] = 'application/json'

    entity = utils.read_json()
    try:
        if utils.validators.validate_albi(entity):
            result = utils.database.add_albi(utils.load_cfg(), entity)
            if result["result"] == "ok":
                return json.dumps(result)
            else:
                raise Exception(result["message"])
    except Exception as e:
        raise bottle.HTTPError(status=500, body=str(e))


def serie():
    bottle.response.headers['Content-type'] = 'application/json'

    entity = utils.read_json()
    # TODO: insert serie into database
