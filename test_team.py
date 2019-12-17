# This Team class is created by Zehua Zheng
# Student Number: 17012373
# a comment added by Zehua Zheng

from unittest import TestCase
from team_class import Team

class TestTeam(TestCase):

    def test_add_member(self):
        id_list = [1, 2, 3, 4, 5, 6]
        id_list_copy_1 = id_list.copy()
        edited_list_1 = Team().add_member(9, id_list)
        id_list_copy_1.append(9)
        self.assertEqual(edited_list_1,id_list_copy_1)

    def test_remove_member(self):
        id_list = [1, 2, 3, 4, 5, 6]
        id_list_copy_2 = id_list.copy()
        edited_list_3 = Team().remove_member(5, id_list)
        id_list_copy_2.remove(5)
        self.assertEqual(edited_list_3,id_list_copy_2)


