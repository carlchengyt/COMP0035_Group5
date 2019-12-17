# This class is created by Yifeng Zhao
# Student Number: 17077657 

from unittest import TestCase

from login import LoginRegister_manager

class TestLoginRegister_manager(TestCase):

    def test_login_validation(self):
        self.assertEqual(LoginRegister_manager("Eric","123abc").Login_validation("Eric","123abc"),True)

    def test_login_validation_false(self):
        self.assertEqual(LoginRegister_manager("Eric","123abc").Login_validation("Eric","abc123"),False)
