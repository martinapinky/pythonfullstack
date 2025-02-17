# 1. Create a dictionary with keys as country names and values as their capital cities. 
# Write a function that takes a country name as input and returns its capital city. If the 
# country is not in the dictionary, return "Country not found".
from collections import Counter


countries_dict = {
    "Uganda": "Kampala",
    "India": "New Delhi",
    "Kenya": "Nairobi",
    "Rwanda": "Kigali"
}

def get_capital(name):
    return countries_dict.get(name, "Country not found")

print(get_capital("Tanzania"))
# 2. Write a function that takes a list of tuples and converts it into a dictionary. Each tuple 
# contains a key and a value. For example, [(1, "one"), (2, "two")] should be converted into 
# {1: "one", 2: "two"}.
def convert_to_dictionary(lst):
    return(dict(lst))

print(convert_to_dictionary([('a', 1), ('b', 2), ('c', 3)]))

# 3. Given the following dictionary of student scores, calculate the average score and output 
# a dictionary with the students’ names and their respective average score.
student_scores = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [70, 75, 80],
    "David": [88, 82, 91]
}

def average_score(dictionary):
    for student, scores in dictionary.items():
        dictionary[student] =  sum(scores) / len(scores)
    return dictionary

print(average_score(student_scores))

# 4. Write a function that merges two dictionaries. If there are duplicate keys, the value 
# from the second dictionary should be taken.
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "d": 5}
# dict1.update(dict2)

merged_dictionary = {**dict1, **dict2}
print(merged_dictionary)

# 5. Write a function that takes a dictionary and a key, and deletes the key-value pair from 
# the dictionary. If the key does not exist, print "Key not found".
def delete_key(dictionary, key):
    dictionary.pop(key, "Key not found")

delete_key(dict1, "c")
print(dict1)

####Use del d[key]

# 6. Write a function to check if a dictionary is empty.
def isEmpty(dictionary):
    return len(dictionary) > 0

print(isEmpty(dict1))

# 7. Write a function to find the key of the maximum value in a dictionary.
my_dictionary = {'a': 2, 'b': 3, 'c': 1}
def max_value_key(dictionary):
    sorted_items = sorted(dictionary.items(), key = lambda item: item[1])
    return sorted_items[-1][1]

print(max_value_key(my_dictionary))

# 8. Write a function that counts the occurrence of each character in a string and returns 
# the result in a dictionary.
def char_count(str):
    count = {}
    for char in str:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

print(char_count("helloooo"))

# 9. Write a function that swaps the keys and values in a dictionary.
def swap(dictionary):
    return {value: key for key, value in dictionary.items()} #################################

print(swap(my_dictionary))

# 10. Write a function that finds the common keys between two dictionaries.
def common_keys(dict1, dict2):
    return dict1.keys() & dict2.keys()

print(common_keys(dict1, dict2))

# 11. Write a function that adds a new key-value pair to a dictionary only if the key does 
# not already exist.
def add_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    return dictionary

print(add_key(dict1, "d", 0))

# 12. Write a function to sort a dictionary by its values in ascending order.
def sort_by_value(dictionary):
    sorted_items = sorted(dictionary.items(), key = lambda item: item[1])
    return sorted_items

print(dict(sort_by_value(dict1)))

# 13. Write a function that removes all the keys with None values in a dictionary.
def remove_nones(dictionary):
    return {key: value for key, value in dictionary.items() if value is not None}
    # dict1 = {}
    # for key, value in dictionary.items():
    #     if value is not None:
    #         dict1[key] = value
    # return dict1

print(remove_nones({'a': 1, 'b': None, 'c': 2}))

# 14. Write a function to find the intersection of two dictionaries (keys and values must be the same).
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "d": 5}
def dict_intersection(dict1, dict2):
    return dict1.items() & dict2.items()

print(dict_intersection(dict1, dict2))

# 15. Write a function that returns the dictionary after updating all values by adding 1.
def add_one(dictionary):
    return {key: value + 1 for key, value in dictionary.items()}
    # for key, value in dictionary.items():
    #     dictionary[key] = value + 1
    # return dictionary

print(add_one(dict1))

# 16. Write a function that returns a dictionary where the keys are unique values of a list, 
# and the values are the count of those elements.
def lst_count(lst):
    return dict(Counter(lst))

print(lst_count([1, 2, 3, 4, 1, 2, 1, 3, 4, 1]))

# 17. Write a function that checks if a given key exists in a dictionary.
def key_exists(dictionary, key):
    return key in dictionary

print(key_exists(dict1, "f"))

# 18. Write a function that takes a dictionary and returns a new dictionary that has all the 
# keys with string values.
# def string_values(dictionary):
#     return {key: str(value) for key, value in dictionary.items()}
def string_values(d):
    filtered_dict = {}
    for k, v in d.items():
        if isinstance(v, str):
            filtered_dict[k] = v
    return filtered_dict


# 19. Write a function to concatenate all values of a dictionary (assuming all values are 
# strings) into a single string.
def values_string(dictionary):
    return " ".join(dictionary.values())

print(values_string(string_values(dict1)))

# 20. Write a function that takes a dictionary and returns a list of keys sorted by their 
# corresponding values
def sorted_keys(dictionary):
    return list(dict(sorted(dictionary.items(), key = lambda item: item[1])).keys())

print(sorted_keys(dict1))
