# zip()

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']

zipped = list(zip(list1, list2))
print(zipped)

unzip = list(zip(*zipped))
print(unzip)

names = ["Anna", "Bob", "John"]
scores = [80, 70, 90]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

scores1 = dict(zip(names, scores))
print(scores1)

# Merging dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "d": 5}

# dict1.update(dict2)

merged_dictionary = {**dict1, **dict2}
print(merged_dictionary)