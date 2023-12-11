#!/usr/bin/env python3

"""
This is the file with which all classes will be tested with
"""
import sys
from models.base_model import BaseModel
from datetime import datetime
import unittest
import inspect

class TestBaseModel(unittest.TestCase):

    def setUpClass(cls):
        cls.setup = inspect.getmembers(BaseModel, inspect.isfunction)

    def setUp(self):
        self.bm = BaseModel()

    def tearDown(self):
        self.bm = None

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
