# This class is created by Yifeng Zhao
# Student Number: 17077657
# a comment is added

class LoginRegister_manager:

    def __init__(self, User_name, Password):
        self.User_name = User_name
        self.Password = Password

    def Login_validation(self, User_name, Password):
        if self.User_name == User_name and self.Password == Password:
            return True
        else:
            return False

    def Registration(self, User_name, Password):
        pass