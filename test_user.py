from unittest import TestCase
from user import User


class TestUser(TestCase):
    def test_add_user_info(self):
        self.assertIs(User('Username').add_user_info('a comment'), 'a comment')
        self.assertNotEqual(User('Username').add_user_info('a comment'), 'not a comment')


