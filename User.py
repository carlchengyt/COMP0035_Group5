class User(object):
    def __init__(self, username):
        self._username = username
        self._user_info = None

    def add_user_info(self,user_info):
        if user_info is not None:
            self._user_info = user_info
            return user_info
