class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email


class AdminUser(User):
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)
        self.admin_level = admin_level

    def get_admin_level(self):
        return self.admin_level


class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_all_users(self):
        return self.users
