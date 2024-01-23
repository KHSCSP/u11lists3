print("\n--- we can access part of a list (or string) ---")
print("--- this is referred to as a 'slice' ---")
words = 'Forescore and seven years ago...'
nums = [10, 11, 12, 13, 14]

print("indces 0:3")
print(words[0:3])
print(nums[0:3])

print("\nindices :2")
print(words[:2])
print(nums[:2])

print("\nindices 2:")
print(words[2:])
print(nums[2:])



print("\n\n-------------------------------------")
print(" --- another data type: tuples ---")
nums = (3, 13, 42, -51)
print("indexed:", nums[0])

# *not* mutable, cannot change just one
# nums[0] = 15
# you would have to reassign the entire tuple
nums = (15, 13, 42, -51)
print("\nreassigned:", nums)