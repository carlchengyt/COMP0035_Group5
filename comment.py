# This class is created by SHIRUI LI
# Student Number: 17050059
# new updates by SHIRUI LI
class Comment:
    def __init__(self, comment_id, content):
        self.comment_id = comment_id
        self.comment_content = content

    def userstory_comment(self, comment_id, content):
        if self.comment_id == comment_id:
            self.comment_content = content
            return True
        else:
            return False

    def backlog_comment(self, comment_id, content):
        if self.comment_id == comment_id:
            self.comment_content = content
            return True
        else:
            return False