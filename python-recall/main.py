# # print('200 is great number') # string
# # print("200 is great number") # string
# # print(2) # integer
# # print(-22) # - integer
# # print(2.99) # float
# # print(2 * 8) # math operations
# from pyexpat.errors import messages
# from re import match
#
# from lists import my_list
#
# # print("20 days are " + str(50) +" minutes") # concatenating str and int
# # print(20*60*24) # math operations
#
# # print(f"20 days are {20*24*60} minutes") # concatenating str and int the right way - will not work in python version 2
#
# # to_minutes = 24 * 60
# # to_seconds = to_minutes * 60
# # calculation_to_units =  to_seconds
# # unit = "seconds"
# #
# # print(f"20 days are {20 * calculation_to_units} {unit}")
# # print(f"30 days are {30 * calculation_to_units} {unit}")
# # print(f"40 days are {40 * calculation_to_units} {unit}")
#
# # calculation_to_units =  to_minutes
# # unit = "minutes"
# #
# # print(f"20 days are {20 * calculation_to_units} {unit}")
# # print(f"30 days are {30 * calculation_to_units} {unit}")
# # print(f"40 days are {40 * calculation_to_units} {unit}")
#
# # calculation_to_units =  to_minutes/24
# # unit = "hours"
# #
# # print(f"20 days are {20 * calculation_to_units} {unit}")
# # print(f"30 days are {30 * calculation_to_units} {unit}")
# # print(f"40 days are {40 * calculation_to_units} {unit}")
#
# # to_minutes = 24 * 60
# # to_seconds = to_minutes * 60
# # to_hours = to_minutes/60
# # # calculation_to_units =  to_hours
# # units = "hours"
# #
# # def days_to_units(days, units):
# #     # calculation_to_units =
# #     print(f"{days} days are {days * calculation_to_units} {units}")
# #     print("All fine")
# #
# # days_to_units(35,"hours")
# # days_to_units(40,"hours")
# # days_to_units(50,"hours")
# # days_to_units(5,"hours")
#
# # Scopes
# # A variable is only available from inside the region it is created
# #
# # def scope_check(num_of_days):
# #     my_var = "Random var inside function"
# #     print(my_var) # internal variable defined inside function
# #     print(num_of_days) # internal variable passed as a parameter
# #     print(units) # global scope variable
# #
# # scope_check(20)
#
# # User inputs
#
#
# # calculation_to_units =  24
# # units = "hours"
# # def days_to_units(days):
# #     return f"{days} days are {days * calculation_to_units} {units}"
# #
# # user_input = input("Enter number of days and will convert it to hours:\n") # inputs allways interpreted as string
# #
# # user_input_number = int(user_input) # so cast it into number here
# #
# # my_var = days_to_units(user_input_number)
# #
# # print(my_var)
#
#
# # if/else conditions and boolean values
# # Validate User inputs We want to avoid or handle values:
# # - which doesn't make sense
# # - could crash our program
# # - could be security risk
#
# # calculation_to_units =  24
# # units = "hours"
# # def days_to_units(days):
# #     condition_check = days > 0
# #     print(type(condition_check))
# #     if condition_check: # use comparison operator to check if number is positive or not
# #         return f"{days} days are {days * calculation_to_units} {units}"
# #     elif days == 0:
# #         return "you've entered 0 so no conversion for you!"
# #     else:
# #         return "you've entered negative value so no conversion for you!"
# #
# # user_input = input("Enter number of days and will convert it to hours:\n") # inputs allways interpreted as string
# #
# # # More input validations
# # # if user_input.isdigit():
# # #     user_input_number = int(user_input) # so cast it into number here
# # #     my_var = days_to_units(user_input_number)
# # #     print(my_var)
# # # else:
# # #     print("your input is not valid number, don't break my program!")
# #
# # # print(type("this is string")) # str
# # # print(type(10)) # int
# # # print(type(1.25)) # float
# #
# # # encapsulate logic in function
# # def validate_and_execute():
# #     if user_input.isdigit():
# #         user_input_number = int(user_input) # so cast it into number here
# #         my_var = days_to_units(user_input_number)
# #         print(my_var)
# #     else:
# #         print("your input is not valid number, don't break my program!")
# #
# # validate_and_execute()
#
# # Encapsulate input validation
# # calculation_to_units =  24
# # units = "hours"
# # def days_to_units(days):
# #     return f"{days} days are {days * calculation_to_units} {units}"
# #
# #
# # user_input = input("Enter number of days and will convert it to hours:\n") # inputs allways interpreted as string
# #
# # def validate_and_execute():
# # # Nested if/else conditions - not a good practice, but sometimes required
# #     if user_input.isdigit():
# #         user_input_number = int(user_input)
# #         condition_check = user_input_number > 0
# #         if condition_check:
# #             my_var = days_to_units(user_input_number)
# #             print(my_var)
# #         elif user_input_number == 0:
# #             print("you've entered 0 so no conversion for you!")
# #         else:
# #             print("you've entered negative value so no conversion for you!")
# #     else:
# #         print("your input is not valid number, don't break my program!")
# #
# # validate_and_execute()
#
# # Error handling with try/catch
# # calculation_to_units =  24
# # units = "hours"
# # def days_to_units(days):
# #     return f"{days} days are {days * calculation_to_units} {units}"
# #
# #
# # user_input = input("Enter number of days and will convert it to hours:\n") # inputs allways interpreted as string
# #
# # def validate_and_execute():
# #     try:
# #         user_input_number = int(user_input)
# #         condition_check = user_input_number > 0
# #         if condition_check:
# #             my_var = days_to_units(user_input_number)
# #             print(my_var)
# #         elif user_input_number == 0:
# #             print("you've entered 0 so no conversion for you!")
# #         else:
# #             print("you've entered negative number, so no conversion for you!")
# #
# #     except ValueError:
# #         print("your input is not valid number, don't break my program!")
# #
# # validate_and_execute()
#
# # Looping
# # calculation_to_units = 24
# # units = "hours"
# #
# # def days_to_units(days):
# #     return f"{days} days are {days * calculation_to_units} {units}"
# #
# # def validate_and_execute():
# #     try:
# #         user_input_number = int(user_input)
# #         condition_check = user_input_number > 0
# #         if condition_check:
# #             my_var = days_to_units(user_input_number)
# #             print(my_var)
# #         elif user_input_number == 0:
# #             print("you've entered 0 so no conversion for you!")
# #         else:
# #             print("you've entered negative number, so no conversion for you!")
# #
# #     except ValueError:
# #         print("your input is not valid number, don't break my program!")
# # # while loops
# #
# # # while True:
# # #     user_input = input("Enter number of days and will convert it to hours:\n")  # inputs allways interpreted as string
# # #     validate_and_execute()
# #
# # user_input = ""
# # while user_input != "exit": # allow user exit the program
# #     user_input = input("Enter number of days and will convert it to hours:\n")  # inputs allways interpreted as string
# #     validate_and_execute()
#
# # Lists and for loops
# # list is data-type in Python for storing multiple elements of data
# # list allows duplicates in data
# # calculation_to_units = 24
# # units = "hours"
# #
# # def days_to_units(days):
# #     return f"{days} days are {days * calculation_to_units} {units}"
# #
# # def validate_and_execute():
# #     try:
# #         user_input_number = int(num_of_days_element)
# #         condition_check = user_input_number > 0
# #         # we want to do conversions only for positive numbers
# #         if condition_check:
# #             my_var = days_to_units(user_input_number)
# #             print(my_var)
# #         elif user_input_number == 0:
# #             print("you've entered 0 so no conversion for you!")
# #         else:
# #             print("you've entered negative number, so no conversion for you!")
# #
# #     except ValueError:
# #         print("your input is not valid number, don't break my program!")
# #
# # user_input = ""
# # while user_input != "exit": # allow user exit the program
# #     user_input = input("Enter number of days as a comma-separated list and will convert it to hours:\n")  # inputs allways interpreted as string
# #     print(user_input.split(", "))
# #     for num_of_days_element in user_input.split(", "): # could access elements in list one by one using for loop
# #         validate_and_execute()
#
# # Comments
# # 1. To give notes in code, if complicated for example
# #  single-line comment
# """multiple-line comments"""
#
# # Sets
# # another built-in data-type of Python
# # as with lists, used to store multiple items of data
# # DO NOT allow duplicate values
#
# # calculation_to_units = 24
# # units = "hours"
# #
# # def days_to_units(days):
# #     return f"{days} days are {days * calculation_to_units} {units}"
# #
# # def validate_and_execute():
# #     try:
# #         user_input_number = int(num_of_days_element)
# #         condition_check = user_input_number > 0
# #         # we want to do conversions only for positive numbers
# #         if condition_check:
# #             my_var = days_to_units(user_input_number)
# #             print(my_var)
# #         elif user_input_number == 0:
# #             print("you've entered 0 so no conversion for you!")
# #         else:
# #             print("you've entered negative number, so no conversion for you!")
# #
# #     except ValueError:
# #         print("your input is not valid number, don't break my program!")
# #
# # user_input = ""
# # while user_input != "exit": # allow user exit the program
# #     user_input = input("Enter number of days as a comma-separated list and will convert it to hours:\n")  # inputs allways interpreted as string
# #     list_of_days = user_input.split(", ")
# #     set_of_days = set(list_of_days) # convert list into set
# #
# #     print(list_of_days, set_of_days)
# #     print(type(list_of_days), type(set_of_days))
# #     for num_of_days_element in set_of_days: # convert a list into set
# #         validate_and_execute()
#
# # lists are defined with []
# # sets are defined with {}
#
# # Standalone Built-in functions
# # print()   Prints to the standard output device
# # input()   Asks user for input
# # set()     Returns a new set
# # int()     Converts a value into an integer number
# # Full list here: https://docs.python.org/3/library/functions.html
#
# # Built-in functions on Data Types
# # - each Data Type has its own built-in functions
# # - which are useful(make sense) only for this specific data type
# # print([1,2].remove(2))
#
# # Dictionary data type
# # Are used to store values in key:value pairs
# # Is a collection which do not allow duplicate values
#
#
# def days_to_units(days, conversion_unit):
#     if conversion_unit == "hours":
#         return f"{days} days are {days * 24} {conversion_unit}"
#     elif conversion_unit == "minutes":
#         return f"{days} days are {days * 24 * 60} {conversion_unit}"
#     else:
#         return "unsupported unit"
#
#
# def validate_and_execute():
#     try:
#         user_input_number = int(days_and_unit_dictionary['days'])
#         unit = days_and_unit_dictionary['unit']
#         condition_check = user_input_number > 0
#         # we want to do conversions only for positive numbers
#         if condition_check:
#             my_var = days_to_units(user_input_number, unit)
#             print(my_var)
#         elif user_input_number == 0:
#             print("you've entered 0 so no conversion for you!")
#         else:
#             print("you've entered negative number, so no conversion for you!")
#
#     except ValueError:
#         print("your input is not valid number, don't break my program!")
#
# user_input = ""
# while user_input != "exit": # allow user exit the program
#     user_input = input("Enter number of days and conversion unit column separated\n")
#     days_and_unit = user_input.split(":")
#
#     days_and_unit_dictionary = {
#         "days": days_and_unit[0],
#         "unit": days_and_unit[1]
#     }
#     print(type(days_and_unit_dictionary)) # prints type dict
#     validate_and_execute()
#
#
# # my_list = ["20","30","100"]
# # print(my_list[2])
# # my_dictionary = {"days": 20, "unit": "hours", "message": "all good"}
# # print(my_dictionary['message'])
#
# # Data types learned summary
# # message = 'enter some text' # string str
# # days = 20                   # integer int
# # price = 9.99                # float
# # valid_number = True         # boolean
# # exit_input = False          # boolean
# # list_of_days = [20,40,30,90,20]# list allow duplicate values
# # list_of_month = ["Jan", "Feb"] # also list but with strings
# # set_of_days = {20,45,100}   # set - does not allow duplicate values
# # days_and_unit = {"days":20, "unit":"hours"} # dict a dictionary
#
# # Why so many data types:
# # - Depending on what you want to achieve in your program
# # - you need a different data type to achieve exactly that

# Modules:
# - Logically organise your Python code
# - Module should contain related code
# - Module is just .py file containing code, that you
# could use in another .py file

# Create module and import statement
# import helper # import whole module
# from helper import validate_and_execute, user_input_message # import single functions and variables from module
# from helper import * # import everything from module
# # import helper as h # import module as alias name
#
# user_input = ""
# while user_input != "exit": # allow user exit the program
#     user_input = input(user_input_message)
#     # user_input = input(h.user_input_message) # use module variable with alias
#     days_and_unit = user_input.split(":")
#
#     days_and_unit_dictionary = {
#         "days": days_and_unit[0],
#         "unit": days_and_unit[1]
#     }
#     print(type(days_and_unit_dictionary)) # prints type dict
#     # helper.validate_and_execute(days_and_unit_dictionary) # this is how reference functions from a module when whole module imported
#     validate_and_execute(days_and_unit_dictionary) # regular use when single function imported from module
#     # h.validate_and_execute(days_and_unit_dictionary) # use module functions with alias

# More on Python modules can be found here: https://docs.python.org/3/tutorial/modules.html#

# Built-in module examples
# import os
# print(os.name)

import logging
# logger = logging.getLogger("MAIN")
# logger.error("Error happened in app")

# Built-in vs Third-Party modules

# Python comes only with a set of built-in modules
# Many more modules out there, which are NOT part of the Python installation
# You need to install these third-party packages
# Built-in modules and Packages are most common ones
# Depending on what application you write, add specific ones

# Where to find these packages ?
# How to install them ?
# search in https://pypi.org

# Module vs Package
# - any Python file is a module
# - package is a collection of modules
# - package must include an __init__.py file
# - __init__.py distinguishes a package from a directory

# The Python Package Index (PyPI)
# - pypi is a repository for third-party Python packages
# - people can publish their packages to this repository
# - so it becomes available to everyone to use
# - a large community means, many people are creating useful modules and make them available for others

# pip
# - pip is a package manager for Python
# use pip install <PackageName> to install package
# use pip uninstall <PackageName> to uninstall package
