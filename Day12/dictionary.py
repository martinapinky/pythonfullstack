# Python dictionary
# unordered before 3.7, now ordered collection of key value pair
# mutable, each key is unique

my_dictionary = {
    "name": "Anna",
    "age": 21,
    "dept": "dev"
}

x = my_dictionary["name"]
print(x)

y = my_dictionary.get("ice", "not found")
print(y)

my_keys = my_dictionary.keys()
print(my_keys)

my_values = my_dictionary.values()
print(my_values)

my_dictionary["name"] = "John"
print(my_dictionary)

# popitem - removes last element in the dictionary
my_dictionary.popitem()
print(my_dictionary)

my_dictionary .update({"dept": "dev"}) # you can add multiple key value pairs
print(my_dictionary)

# clear
# my_dictionary.clear()
print(my_dictionary)

# looping
for i in my_dictionary:
    print(my_dictionary[i])

for j in my_dictionary.keys():
    print(j)

for x, y in my_dictionary.items():
    print(x, y)

## Print the dictionary 1 to 5
# n = int(input("Enter a number"))
# d = dict()
# for x in range(1, n + 1):
#     d[x] = x * x

# print(d)

# if key is present
# def is_key_present(x):
#     if x in d:
#         print("key is present")
#     else:
#         print("Not present")

# is_key_present(5)

# copy
new_dictionary = my_dictionary.copy()
print(new_dictionary)

# sort the dictionary by values
d = {"a": 200,
     "b": 300,
     "c": 100,
     "d": 700}

sorted_items = sorted(d.items(), key = lambda item: item[1])
print(sorted_items)

key_min = sorted_items[0][0]
min_value = sorted_items[0][1]
print(key_min)
print(min_value)

str = "helloooo"
char_count = {}

for char in str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

space_dict = {'first   name': 'john', 'last  name': 'Doe'}

# for i, 