#!/usr/bin/python3
"""the test module for User class"""
import unittest

from models.city import City


class TestUser(unittest.TestCase):
    """TestUser class for testing the User instance"""

    city_model = City()

    def setUp(self):
        """set up method for instance info"""
        self.city_model.state_id = "123-4456"
        self.city_model.name = "Lagos"

    def test_user_info(self):
        """tests the information of user"""
        state_id = self.city_model.state_id
        name = self.city_model.name
        self.assertEqual(state_id, "123-4456")
        self.assertEqual(name, "Lagos")

    def test_user_info_type(self):
        """tests for the type of the information"""
        self.assertIsInstance(self.city_model.state_id, str)
        self.assertIsInstance(self.city_model.name, str)
