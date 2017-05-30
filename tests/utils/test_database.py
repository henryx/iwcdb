# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see LICENSE for details)
"""

import unittest

from unittest import mock
import src.utils.database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        pass

    @mock.patch("src.utils.database.Database.__init__.psycopg2.connect")
    def test_database(self, mock_psycopg2_connect):
        data = {"database": {}}
        data["database"]["host"] = "localhost"
        data["database"]["port"] = 5432
        data["database"]["database"] = "fakedb"
        data["database"]["user"] = "fakeuser"
        data["database"]["password"] = "fakepwd"

        database_mock = mock.Mock()
        mock_psycopg2_connect.return_value = database_mock
        d = src.utils.database.Database(data)
        database_mock.assert_called_with(d)
