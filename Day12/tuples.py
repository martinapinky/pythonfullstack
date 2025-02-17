# Tuples: immutable, ordered, indexed
# similar to list

# gps coordinates (latitude, longitude)
# status codes 500, 200, 404 ...etc

# created using parenthesis
my_tuple = (1, 2, 4, 5)
print(my_tuple)

mytuple = (1, "Anna", True, 3002)
print(mytuple)

print(type(mytuple))
print(mytuple[0])
print(mytuple[-1])

# Slicing a tiple
print(mytuple[1:4])

# Unpack allows assigning tuple elements to multiple variables
id, name, isEmployed, salary = mytuple
print(name)
print(isEmployed)

for ele in mytuple:
    print(ele)

# Built in methods
# count() --> count occurences
tuple_numbers = (1, 2, 3, 2, 1, 4, 2, 1)#
print(tuple_numbers.count(1))

#index --> first occurence
print(tuple_numbers.index(4))

# tuple_numbers[0] = 100   # --> Type error

# tuples can be nested
my_tuple = (1, (2, 3), (4, 5))
print(my_tuple)

lst = list(my_tuple)
print(lst)

tuple1 = tuple(lst)
print(tuple1)

# faster than list, consume less memory, can be used as key because the hash value cannot be changed
{
    (): "value"
}

# Remove empty tuple(s) from a list of tuples
LstTuples = [(), (), (), (''), ('a', 'b'), ('a', 'b', 'c')]
removeEmpty = [t for t in LstTuples if t]
print(removeEmpty)

# Compare two tuples lexiographically
a = (1, 2, 3)
b = (1, 2, 4)
print(a < b)

# Sum --> built in method
print(sum(a))

# reverse a tuple
print(tuple(reversed(a)))

# max and min
print(max(a))

