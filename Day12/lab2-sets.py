# 1. Create a set
# Create a set with elements {1, 2, 3, 4, 5} and print it.
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. Add an element
# Add the element 6 to the set and print the updated set.
my_set.add(6)
print(my_set)

# 3. Remove an element
# Remove the element 3 from the set and print the updated set.
my_set.remove(3)
print(my_set)

# 4. Discard an element (no error if not present)
# Discard the element 10 from the set and print the updated set.
my_set.discard(10)
print(my_set)

# 5. Check if elements exist
# Check if elements 3 and 6 exist in the set and print the results.
set1 = {3}
set2 = {6}
print(f"3 {'exists' if set1.issubset(my_set) else 'does not exist'} in the set {my_set}")
print(f"6 {'exists' if set2.issubset(my_set) else 'does not exist'} in the set {my_set}")

# 6. Find the length of the set
# Create a set {1, 2, 3, 4, 5, 5, 6}, print its length, and observe how duplicates are handled.
new_set = {1, 2, 3, 4, 5, 5, 6}
print(len(new_set))

# 7. Set difference
# Find the difference between sets {1, 2, 3, 4} and {3, 4, 5, 6} and print the result.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b)

# 8. Set union
# Find the union of sets {1, 2, 3, 4} and {3, 4, 5, 6} and print the result.
print(a | b)

# 9. Set intersection
# Find the intersection of sets {1, 2, 3, 4} and {3, 4, 5, 6} and print the result.
print(a & b)

# 10. Symmetric difference
# Find the symmetric difference between sets {1, 2, 3, 4} and {3, 4, 5, 6} and print the result.
print(a.symmetric_difference(b))

# 11. Subset check
# Check if {1, 2} is a subset of {1, 2, 3, 4} and print the result.
c = {1, 2}
print(c.issubset(a))

# 12. uperset check
# Check if {1, 2, 3, 4} is a superset of {1, 2} and print the result.
print(a.issuperset(c))

# 13. Disjoint sets check
# Check if sets {1, 2, 3} and {4, 5, 6} are disjoint and print the result.
d = {1, 2, 3}
e = {4, 5, 6}
print(d.isdisjoint(e))

# 14. Copy a set
# Copy set {1, 2, 3, 4} into another variable and check if they are different objects.
f = a.copy()
print(a == f)

# 15. Pop an element
# Remove a random element from the set {10, 20, 30, 40, 50} using pop() and print the removed element.
number_set = {50, 20, 30, 40, 10}
print(number_set.pop())

# 16. Clear a set
# Clear all elements from a set and print the empty set.
number_set.clear()
print(number_set)

# 17. Update a set
# Update the set {1, 2, 3} with elements {4, 5, 6} and print the updated set.
d.update(e)
print(d)

# 18. Difference update
# Remove elements from {1, 2, 3, 4, 5} that are also present in {3, 4, 5, 6, 7} using difference_update().
my_set = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 5, 6, 7}
my_set.difference_update(my_set2)
print(my_set)

# 19. Intersection update
# Retain only elements in {1, 2, 3, 4, 5} that are also in {3, 4, 5, 6, 7} using intersection_update().
my_set = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 5, 6, 7}
my_set.intersection_update(my_set2)
print(my_set)

# 20. Symmetric difference update
# Update set {1, 2, 3} to contain only elements that are in either {1, 2, 3} or {2, 3, 4} but not both.
d = {1, 2, 3}
e = {2, 3, 4}
d.symmetric_difference_update(e)
print(d)