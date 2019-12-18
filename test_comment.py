# This Team class is created by SHIRUI LI
# Student Number: 17050059
# new updates
from unittest import TestCase
from comment import Comment

class TestComment(TestCase):

    def test_userstory_comment_validation(self):
        self.assertEqual(Comment('123', 'abc').userstory_comment('123', 'abc'), True)

    def test_backlog_comment_false(self):
        self.assertEqual(Comment('123', 'abc').backlog_comment('123', 'abc'), True)


