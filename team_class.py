# This Team class is created by Zehua Zheng
# Student Number: 17012373
# new change


class Team:

    def __init__(self):
        member_id = 0
        id_list = []

    def add_member(self, member_id, id_list):
        for i in range(len(id_list)):
            if id_list[i] == member_id:
                print('member is already in the team')
                return False
        id_list.append(member_id)
        return id_list


    def remove_member(self, member_id, id_list):
        for j in range(len(id_list)):
            if id_list[j] == member_id:
                id_list.remove(member_id)
                return id_list
        return False





