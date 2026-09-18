my_set = {"January", "February", "March"}
# Basic Set operations
#  - create a set
#  - access items only via loop !!!
#  - add an item to a set
#  - remove an item from the set
# Unordered and unchangeable !!!
# - items in a set DO NOT have an order
# - items can NOt be referred by index
# - items can NOT be changed, only added/removed
for element in my_set:
    print(element)

my_set.add("April") # adding elements
print(my_set)

my_set.remove("January") # remove item from set
print(my_set)
# Quick example for removing items from a list
my_list = list(my_set)
print(my_list)
my_list.remove("March")
print(my_list)