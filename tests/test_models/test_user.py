#!/usr/bin/python3
"""the test module for User class"""
import unittest

from models.user import User


class TestUser(unittest.TestCase):
    """TestUser class for testing the User instance"""

    user_model = User()

    def setUp(self):
        """set up method for instance info"""
        self.user_model.email = "email@mail.com"
        self.user_model.first_name = "Foo"
        self.user_model.last_name = "Bar"
        self.user_model.password = "12345"

    def test_user_info(self):
        """tests the information of user"""
        email = self.user_model.email
        first_name = self.user_model.first_name
        last_name = self.user_model.last_name
        password = self.user_model.password
        self.assertEqual(email, "email@mail.com")
        self.assertEqual(first_name, "Foo")
        self.assertEqual(last_name, "Bar")
        self.assertEqual(password, "12345")

    def test_user_info_type(self):
        """tests for the type of the information"""
        self.assertIsInstance(self.user_model.first_name, str)
        self.assertIsInstance(self.user_model.last_name, str)
        self.assertIsInstance(self.user_model.email, str)
        self.assertIsInstance(self.user_model.password, str)
