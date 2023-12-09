#!/usr/bin/env python3

"""
This is the file with which all classes will be tested with
"""
import sys
import os
from models.base_model import BaseModel
from datetime import datetime
import unittest

c_dir = os.path.models(os.path.realpath(__file__))
sys.path.append(c_dir)


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
