from functools import reduce
import re
import random

# Sum Items in List
numbers = [1, 2, 3, 4, 5]
def sumItems(lst):
    return reduce(lambda total, num: total + num, numbers)

print(sumItems(numbers))

# Multiply Items in List
def multiplyItems(lst):
    return list(map(lambda num: num * 2, lst))

print(multiplyItems(numbers))

# Get Largest Number in List
def largestNumber(lst):
    return reduce(lambda largest, num: num if num > largest else largest, lst)

print(largestNumber(numbers))

# Get Smallest Number in List
def smallestNumber(lst):
    return reduce(lambda smallest, num: num if num < smallest else smallest, lst)

print(smallestNumber(numbers))

# Count Strings with Same Start and End
words = ["abc", "xyz", "aba", "1221"]

def sameStartEndCount(lst):
    regex = r"^(.).*\1$"
    return len(list(filter(lambda str: re.match(regex, str),  lst)))

print(sameStartEndCount(words))

######################################### Sort Tuples by Last Element

# Remove Duplicates from List
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 5, 5]
def removeDuplicates(lst):
    return list(set(lst))

print(removeDuplicates(numbers))

# Check if List is Empty
def isEmpty(lst):
    return len(lst) < 0

print(isEmpty(numbers))

# Clone or Copy a List
words2 = words.copy()
print(words2)

# Find Words Longer Than n
fruits = ["apple", "banana", "cherry", "date"]
def words_longer_than_n(lst, n):
    return list(filter(lambda word: len(word) > n, lst))

print(words_longer_than_n(fruits, 5))

# Check Common Member Between Two Lists
def common_members(lst1, lst2):
    return any([item in lst1 for item in lst2])    ##########################################

print(common_members(numbers, fruits))

# Remove Specific Elements from List
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
def remove_specific_indices(lst, indicesSet):
    return [item for i, item in enumerate(lst) if i not in indicesSet]

print(remove_specific_indices(colors, {0, 4, 5}))

################################################ Generate 3D Array

# Remove Even Numbers from List
def remove_even_numbers(lst):
    return [num for num in lst if num % 2 == 1]

print(remove_even_numbers(numbers))

# Shuffle a List Randomly
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

numbers = [1, 2, 3, 4, 5]
print(shuffle_list(numbers))

# Find Second Largest Number in List
def second_largest(lst):
    lst.sort()
    return lst[-2]

print(second_largest(numbers))

# Find the Second Smallest Number in a List
def second_smallest(lst):
    lst.sort()
    return lst[1]

print(second_smallest(numbers))

# Reverse a List Without Using reverse() Method
def reverse_list(lst):
    return [lst[len(lst) - 1 - i] for i in range(len(lst))]

print(reverse_list(numbers))

# Find the Cumulative Sum of a List
def cumulative_sum(lst):
    return reduce(lambda total, num: total + num, numbers) 

print(cumulative_sum(numbers))

# Find the Intersection of Two Lists
numbers2 = [5, 6, 7, 8, 9, 0]
def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))    ################################

print("Set Intersection: ", list_intersection(numbers, numbers2))

# Remove All Occurrences of a Given Element from a List
numbers3 = [1, 2, 3, 4, 2, 2]
def remove_element(lst, element):
    return [num for num in lst if num != element]

print(remove_element(numbers3, 2))

################################################## Convert a List of Tuples into a Dictionary

# Find the Difference Between Two Lists
def difference_btn_lists(lst1, lst2):
    intersection = list(set(lst1) & set(lst2))
    return [item for item in lst1 if item not in intersection] + [item for item in lst2 if item not in intersection]

print("Difference between the lists: ",difference_btn_lists(numbers, numbers2))

# Find the Union of Two Lists
def list_union(lst1, lst2):
    return list(set(lst1).union(set(lst2))) 

print("Set Union: ", list_union(numbers, numbers2))

##################################################### Convert a List into a Set

# Find the Frequency of Each Element in a List
from collections import Counter

def frequency_dict(lst):
    return dict(Counter(lst))

print(frequency_dict([1, 2, 2, 3, 3, 3, 4])) 

# Find the Most Common Element in a List
def most_common_element(lst):
    frequency_dictionary = dict(Counter(lst))
    return max(frequency_dictionary, key=frequency_dictionary.get)  ###################################################

print("Most common element: ", most_common_element([1, 2, 2, 3, 3, 3, 4]))


# Find the Least Common Element in a List
def least_common_element(lst):
    frequency_dictionary = dict(Counter(lst))
    return min(frequency_dictionary, key=frequency_dictionary.get)

print("Least common element: ", least_common_element([1, 2, 2, 3, 3, 3, 4])) #########################################


########################################################### Sort a List in Descending Order
reversed_lst = sorted(numbers, reverse=True)

# Find the Average of Numbers in a List
def average_number(lst):
    return sum(lst) / len(lst) if numbers else 0

# Count Occurrences of an Element in a List
def number_of_occurences(lst, element):
    return lst.count(element)

print(number_of_occurences([1, 2, 2, 3, 3, 3, 4], 3))

# Convert a List of Lists into a Single List
def flatten_list(lst):
    return reduce(lambda flattened_lst, lst_element: flattened_lst + lst_element, lst)

print(flatten_list([[1, 2], [3, 4], [5, 6]]))

# Check If a List Contains Only Unique Elements
def contains_unique(lst):
    return lst == set(lst)
    # frequency_dictionary = dict(Counter(lst))
    # return max(frequency_dictionary.values()) <= 1
    
print(contains_unique(numbers3))

# Rotate a List to the Left by n Places
def rotate_left(lst, n):
    return lst[n:] + lst[:n]

print(rotate_left([1, 2, 3, 4, 5], 2))  # Output: [3, 4, 5, 1, 2]

# Rotate a List to the Right by n Places
def rotate_right(lst, n):
    return lst[-n:] + lst[:-n]

print(rotate_right([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]


# Find the Difference Between the Largest and Smallest Number in a List
def difference_btn_max_min(lst):
    return max(lst) - min(lst)

print(difference_btn_max_min([1, 2, 3, 4, 5]))


print(numbers)

sorted_lst = sorted(numbers, reverse=True)
print(sorted_lst)