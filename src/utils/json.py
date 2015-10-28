# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see GPL.txt for details)
"""

__author__ = 'enrico'

import json


def validate(func):
    def inner(self, **kwargs):
        types = func.__annotations__
        for argname in kwargs:
            curarg = kwargs[argname]
            curtype = types[argname]
            if not isinstance(curarg, curtype):
                raise ValueError('{} is {}, not {}!'.format(argname, curarg, curtype))
        return func(self, *kwargs)

    return inner


class Json:
    @validate
    def __init__(self, uno: int, due: str, tre: list):
        self.uno = uno
        self.due = due
        self.tre = tre


# Example
if __name__ == "__main__":
    j = Json(**json.loads('{"uno": 1, "due": "due", "tre": [1]}'))
    print(j.uno)
