# Python sets
# no duplicate values
# mutable(can add/remove elements)
# unordered -- > do not have definite order

my_set = {7, 1, "Hello", 5, 3}
print(my_set)
print(type(my_set))

# set methods
# add elements
my_set.add(4)
print(my_set)

my_set.update([5, 6, 7])  # add multiple values
print(my_set)

# my_set.remove(2)  # will throw key error for elements that do not exist
my_set.discard(2)  # does not throw error
print(my_set)

# pop
element = my_set.pop()
print(f"removed: {element}")
print(my_set)

# clear
my_set.clear()
print(my_set)

# Set Operations
# union --> combines (OR | operator)

a = {1, 2, 3}
b = {2, 3, 6}
print(a.union(b))
print(a|b)
print(a)
print(b)

# Intersection
print(a.intersection(b))
print(a & b)

# difference
print(a - b)
print(a.difference(b))

# subset
print(a.issubset(b))
# print(a.isproperset(b)) #in built method not there

c = {2, 3, 4}
d = {2, 3}
print(c.issuperset(d))

# isdisjoint() --> checks if two sets have no common elements
print(c.isdisjoint(d))

print(a.symmetric_difference(b))

a = {2, 3}
b = {2, 3}
def is_proper_set(a, b):
    return b.issubset(a) and a != b

print(is_proper_set(a, b))

# copy() creates copy

copy_set = c.copy()
print(copy_set)

# Frozen sets (immutable)
frozen = frozenset([1, 2, 3])
frozen.add(5)