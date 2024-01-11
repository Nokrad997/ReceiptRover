class LoginView:
    def display_login_prompt(self):
        print("Welcome! Please log in.")

    def get_username(self, username):
        print(f"Using provided username: {username}")
        return username

    def get_password(self, password):
        print(f"Using provided password: {password}")
        return password
