class User:
    def __init__(self, user_id, username, password):
        self._user_id = user_id
        self._username = username
        self._password = password

    @property
    def user_id(self):
        return self._user_id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @username.setter
    def username(self, value):
        self._username = value

    @password.setter
    def password(self, value):
        self._password = value
