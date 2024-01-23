import random

print("\n\n-------------------------------------")
print(" --- slicing ---")
nums = [random.randint(10,100) for i in range(15)]
print("the list:", nums)
# experiment with slicing
print("a few near the beginning:")
print("a few near the middle:")
print("a few near the end:")


# loop through a slice
print("\n\nlooping through a slice:")


print("\n\n-------------------------------------")
print(" --- copying ---")
# 'copy' a list using assignment
# (remember, this is actually a pointer to the same memory, not a copy of the data)
print("\n\n'copying' a list using assignment:")

print("changing one list changes both!")




# copy using list comprehension
print("\n\ncopy using comprehension:")
print("this copies each item into a new list")




# copy a list using slicing
print("\n\ncopying usoing slicing")
print("this copies each item into a new list")



# copy using .copy() (probably skip)



print("\n\n-------------------------------------")
print(" --- tuples ---")
# ask for 3 numbers, create a tuple (r,g,b)
# calculate the average of the values
# loop through and print
# try to change an item using its index
# change the tuple

