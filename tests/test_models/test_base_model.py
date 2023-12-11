#!/usr/bin/python3
"""test BaseModel module"""
import datetime
import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test class for the BaseModel"""

    model = BaseModel()

    def test_unique_id(self):
        """tests for unique ids"""
        u_ids = set()
        for _id in range(200):
            u_id_model = BaseModel()
            self.assertNotIn(u_id_model.id, u_ids)
            u_ids.add(u_id_model.id)

    def test_id_str(self):
        """tests the type of id"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """tests for creation date type"""
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at(self):
        """tests for update date type"""
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    # def test_print(self):
    #     """test for string method"""
    #     self.assertEqual()
