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



print("\n\n-------------------------------------")
print(" --- try this ---")
s1 = "Hello world!"
s2 = "Goodbye blue Monday"
# display the first two characters of s1
# display the last two characters of s2
# join together the first two characters of s1 and the last two characters of s2



print("\n\n")
# given a list of accounts and login dates
# make a list of accounts that 
# have not been logged into in 2024
accounts = ["oakemployee, 5/26/2021", 
         "walrusschedule, 11/2/2024",
         "containspikes, 4/12/2023", 
         "offensiveearrings, 7/31/2024",
         "closerpatience, 6/26/2021",
         "passpizza, 8/24/2021",
         "officialexperiment, 8/28/2022",
         "jabqualify, 3/18/2022",
         "fordhunt, 4/4/2024",
         "snoozeguitar, 11/27/2024",
         "rareseamstress, 8/17/2024"]










# ----- summary ----
print("\n----- summary -----")
print("to remove unwanted items from a list:")
print("\tmake a new list")
print("\tloop through the original list")
print("\tonly append to the new list if you want that item")
print("\tnote: .remove() only removes the *first* occurance of an item")

print("\nto remove unwanted items from a string")
print("\tuse .replace() which replaces all occurances")