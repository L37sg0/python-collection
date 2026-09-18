# # Classes and objects
#
# # User information
# email = "em@em.com"
# name = "John Wick"
# password = "pwd"
# current_job_title = "Engineer"
#
# # User behaviour
# def change_password():
#     # do smth
# def change_job_title():
#     # do smth
# def add_new_skill():
#     # do smth
#
# # Blueprint for a User is called a class
# # Specific implementation of the User is called an object

# Classes
# - class is like an object constructor
# - all classes have a __init__() function
# - __init__() is executed automatically, whenever
# we create the object from this class

# "self" Parameter
# - self is a reference to the current instance of the class
# - is used to access variables that belong to the class

# Each class is in separate file with <lowercase-class>.py as file-name
# and class <Class> definition

# Create an object from a class
from user import User # Import a class
from post import Post # Import class

user_one = User("em@em.com", "John Wick", "pwd", "Engineer")
user_one.get_user_info()
user_one.change_job_title("DevOps trainer")
user_one.get_user_info()

user_two = User("ab.li@em.com", "Abraham Lincoln", "pwd2", "Construction worker")
user_two.get_user_info

post1 = Post("on a secret mission today", user_one.name)
post2 = Post("on a secret mission today", user_two.name)

post1.get_post_info()
post2.get_post_info()