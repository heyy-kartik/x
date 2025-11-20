# 1. Creating a Tuple
my_tuple = (10, 20, 30, 40, 50)
print("Original Tuple:", my_tuple)

# 2. Accessing Elements
print("First Element:", my_tuple[0])
print("Third Element:", my_tuple[2])

# 3. Slicing
print("Slice (1:4):", my_tuple[1:4])
print("First 3 elements:", my_tuple[:3])
print("Last 2 elements:", my_tuple[-2:])

# 4. Length of Tuple
print("Length:", len(my_tuple))

# 5. Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Concatenated Tuple:", tuple1 + tuple2)

# 6. Repetition
print("Repetition:", (5, 10) * 3)

# 7. Membership
print("Is 20 in my_tuple?", 20 in my_tuple)
print("Is 100 in my_tuple?", 100 in my_tuple)

# 8. Iteration
print("Iterating over tuple:")
for item in my_tuple:
    print(item)

# 9. Mixed Data Types
mixed = (10, "hello", 3.14, True)
print("Mixed Tuple:", mixed)

# 10. Nested Tuple
nested = (1, 2, (3, 4, 5))
print("Nested Tuple Element (nested[2][1]):", nested[2][1])

# 11. Count and Index
nums = (1, 2, 3, 2, 4, 2)
print("Count of 2:", nums.count(2))
print("Index of 3:", nums.index(3))

# 12. Immutability (Demonstration)
print("Tuples are immutable. You cannot change elements.")