class User:
    def __init__(self, email, name, password, current_job_title): # Constructor
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password
    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title
    def get_user_info(self):
        print(f"User {self.name} currently works as {self.current_job_title}. You can contact em at {self.email}")


# # Create an object from a class
# user_one = User("em@em.com", "John Wick", "pwd", "Engineer")
# user_one.get_user_info()
# user_one.change_job_title("DevOps trainer")
# user_one.get_user_info()