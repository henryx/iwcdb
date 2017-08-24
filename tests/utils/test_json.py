# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see LICENSE for details)
"""

import unittest
import src.utils.validators


class TestJson(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_validate_albi_1(self):
        data = {"serie": 1,
                "numero": 2,
                "uscita": "2017-01-01",
                "prezzo": 4}

        self.assertTrue(src.utils.json.validate_albi(data))

    def test_validate_albi_2(self):
        data = {"test": 1}

        with self.assertRaises(ValueError) as context:
            src.utils.json.validate_albi(data)

        self.assertTrue("is missing in JSON" in str(context.exception))

    def test_validate_albi_3(self):
        data = {"serie": 1,
                "numero": 2,
                "uscita": "2017-13-01",
                "prezzo": 4}

        with self.assertRaises(ValueError) as context:
            src.utils.json.validate_albi(data)

        self.assertTrue("Malformed date" in str(context.exception))
