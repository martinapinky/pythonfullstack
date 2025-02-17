# list --> python --> most commonly used data type
# ordered items, indexed, mutable, allows duplicate

lst = [1, 2, 3, 4, 5]
print(lst)

# mixed data types
mixed_list = [1, "Hello", 5]

# nested list
nested_list = [1, 2, 3, 4, [5, 6]]

print(lst[0])
print(nested_list[4][1])

# changing the element
lst[1] = 8
print(lst)

# Adding the element at the end of the list
lst.append(50)
print(lst)

# Use insert
lst.insert(2, 17)
print(lst)

# extend
lst.extend([60, 70])
print(lst)

lst2 = [80, 90]
lst.extend(lst2)
print(lst)

# remove
# remove first occurance
lst.remove(50)
print(lst)

# pop ---> removes element at specific index
lst.pop(3)
print(lst)

lst.pop(3)
print(lst)

lst3 = [1, 2, 3, 4]
lst4 = [5, 6, 7, 8]
result = lst3 + lst3
print(result)
print(lst3)
print(lst4)

# Membershing (in, not in) --> check if a item in
print(2 in lst)
print(2 not in lst)

# list comprehension

# create a list of square from 0 to 4
squares = [x**2 for x in range(5)]
print(squares)

# create list for even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Lamda functions
# Anonymous small function, use lambda keyword
# short operations that are passed as argument

doubled_numbers = lambda x: x * 2
print(doubled_numbers(5))

lst = [1, 3, 5, 6, 7]
doubled_numbers = list(map(lambda x: x * 2, lst))
print(doubled_numbers)

numbers = [1, 2, 3, 4, 5]
even_number = list(filter(lambda x: x % 2 == 0, numbers))
print(even_number)

words = ["apple", "banana", "cherry"]
firsta = list(filter(lambda word: word.startswith("a"), words))
print(firsta)

str = "hello"
uppercase = list(map(lambda char: char.upper(), str))
print(uppercase)

filteredString = "".join(list(filter(lambda char: char not in ["a", "e", "i", "o", "u"], str)))
print(filteredString)

from functools import reduce

array = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, array)
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
count = reduce(lambda accumulator, item: accumulator.update({item: accumulator.get(item, 0) + 1}) or accumulator, items, {})
print(count)  