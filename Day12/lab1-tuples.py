# Create a tuple with different data types and print it.
mytuple = (1, "Anna", True, 3002)
print(mytuple)

# Access the second element in a tuple.
print(tuple[1])

# Try modifying a tuple element and observe the error.
# mytuple[0] = 100   # --> Type error

# Convert a list to a tuple.
lst = list(mytuple)
print(lst)

# Find the length of a tuple.
print(len(mytuple))

# Concatenate two tuples.
my_tuple = (1, 2, 4, 5)
concatenated_tuple = mytuple + my_tuple
print(concatenated_tuple)

# Repeat a tuple 3 times.
print(my_tuple * 3)

# Check if an element exists in a tuple.
print(my_tuple.count(6) > 0)

# Unpack a tuple into variables.
id, name, isEmployed, salary = mytuple
print(name)
print(isEmployed)

# Slice a tuple from index 1 to 3.
print(my_tuple[1:3])

# Find the index of an element in a tuple.
tuple_numbers = (1, 2, 3, 2, 1, 4, 2, 1)
print(tuple_numbers.index(4))

# Count the occurrences of an element in a tuple.
print(tuple_numbers.count(1))

# Convert a tuple into a string.
print(str(mytuple))

# Create a nested tuple.
my_tuple = (1, (2, 3), (4, 5))
print(my_tuple)

# Iterate through a tuple using a loop.
for element in mytuple:
    print(element)

# Find the maximum and minimum values in a numeric tuple.
print(max(tuple_numbers))
print(min(tuple_numbers))

# Reverse a tuple.
print(tuple(reversed(my_tuple)))

# Find the sum of elements in a numeric tuple.
print(sum(tuple_numbers))

# Convert a tuple of tuples into a dictionary.
tuple1 = (('a',1), ('b', 2), ('c', 3))
print(dict(tuple1))

# Compare two tuples lexicographically.
a = (1, 3, 3)
b = (2, 2, 4)
print(a > b)