# Strings
a = "Hello World"
a = 15  # datatype changes to int
print(type(a))

# multiline string
a = """Lorem
ipsum
dolor"""
print(a)

# single quotes
a = 'hill'
print(a)

# String  indexing
print(a[1])
print(a[-1]) # negative indexing

# python slicing
# Slicing
a = "Hello World"
print(a[2:4])  # the end, 4 is not included
print(a[2:7:2]) # last 2 is the gap loW is printed
print(a[:5])  # starting from 0 to before 5

print(a[::-1]) #reversing the string
print(a[2:])

# convert string to uppercase
print(a.upper())
print(a.lower())

a = " Hello World  "
print(a.strip())  # trim white spaces

# replace character
print(a.replace("H", "J"))

# empty separator does not work
# print(a.split(""))

# separates words into a list
print(a.split())

# string concatenation
str1 = "hello"
str2 = "world"
print(str1 + " " + str2)
print(str1 * 3)

# length of the string
print(len(str1))

# escape characters
a = "Hello\nWorld"
a = "hello\tworld"
print(a)

print(a.title())

s = "   hello world hello   "
print(s.lstrip())
print(s.rstrip())

# find
print(s.find("hello"))  # returns the index if string exists
print(s.rfind("hello"))  # returns the last index string exists
print(s.find("us"))  # returns -1 if string doesn't exist

# count
print(s.count("x"))

strdigit = "1234"
print(strdigit.isdigit())

stralpha = "hello"
print(stralpha.isalpha())

stralphanum = "hello123"
print(stralphanum.isalnum())

print(s.startswith("hello"))
print(s.endswith("world"))

# zfill --> pads the string with zeros
s = "42"
print(s.zfill(5))

# just
p = "Hello"
print(p.rjust(10))
print(p.ljust(10))
print(p.center(10))

# String indexing
# Access individual characters
s = "Hello"
for char in s:
    print(char)

for index, char in enumerate(s):
    print(f"Index: {index}, character {char}")

for index in range(len(s)):
    char = s[index]
    print(f"Index: {index}, character {char}")

# while loop
index = 0
while index < len(s):
    print(s[index])
    index += 1   # ++ not supported in python

print(tuple(zip(range(len(s)), s)))
for index, char in zip(range(len(s)), s):
    print(f"Index: {index}, character {char}")