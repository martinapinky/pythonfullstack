# enumerate --> built in function for tracking of index and element
# while iterating

# enumerate(iteratable, start=0)  ---> iteratables include list. tuple, string

fruits = ['apple', 'banana', 'cherry']

for index, value in enumerate(fruits, start=1):
    print(index, value)



from enum import Enum

class color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(color.RED.value)
print(color.GREEN.value)
print(color.BLUE.value)