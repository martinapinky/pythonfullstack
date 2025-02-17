# Iterator
# is an object that contains a countable number of values(ie you can traverse through the values)

# 1. Iterable: is an object that can return an iterator such as list, dict

# 2. Iterator: implements the iterator protocol
# --> consists of 2 methods
# __iter__(): return the iterator object itself
# __next__(): return the next value in sequence

# Custom Iterator that counts down to 1 from a specified number
class CountdownIterator:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self
    # behaviour of loop
    def __next__(self):
        if self.start > 0:
            current = self.start
            self.start -= 1
            return current
        raise StopIteration
    
countdown_iter = CountdownIterator(5)

for number in countdown_iter:
    print(number)

# Custom iterator that returns the squares of the numbers until it reaches the end of the list
class SquareIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self
    # behaviour of loop
    def __next__(self):
        if self.index < len(numbers):
            square = self.numbers[self.index] ** 2
            self.index += 1
            return square
        raise StopIteration
    
numbers = [1, 2, 3, 4, 5]

square_iter = SquareIterator(numbers)
# print(list(square_iter))
for square in square_iter:
    print(square)