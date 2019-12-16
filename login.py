class LoginRegister_manager:
    # This class is created by Yifeng Zhao
    def __init__(self, User_name, Password):
        self.User_name = "username"
        self.Password = "password"

    def Login_validation(self, User_name, Password):
        if self.User_name == User_name and self.Password == Password:
            return True
        else:
            return False