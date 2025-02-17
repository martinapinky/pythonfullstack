# Exercises 

# How to reverse a string in Python?
str = "Hello World"
print(str[::-1])

# How to check if a string is a palindrome?
print(str[::-1] == str)

# How to count occurrences of a substring in a string?
print(str.count("l"))
print(str.count("ll"))

# How to check if a string contains only digits?
print(str.isdigit())

# How to convert a string to uppercase?
print(str.upper())

# How to convert a string to lowercase?
print(str.lower())

# How to capitalize the first letter of each word in a string?
print(str.title())

# How to remove leading and trailing whitespaces from a string?
print(str.strip())

# How to replace all occurrences of a substring with another substring?
print(str.replace("l", "1"))

# How to find the index of the first occurrence of a substring?
print(str.find("Wo"))

# How to check if a string starts with a specific substring?
print(str.startswith("Hel"))

# How to check if a string ends with a specific substring?
print(str.endswith("rld"))

# How to split a string by a delimiter?
print(str.split(" "))

# How to join a list of strings into a single string?
list = ["Hello", "World"]
print(" ".join(list))

# How to check if a string contains only alphabetic characters?
print(str.isalpha())

# How to check if a string contains only alphanumeric characters?
print(str.isalnum())

# How to remove all vowels from a string?
newString = ""
for char in str:
    vowels = "aeiou"
    if vowels.count(char) == 0:
        newString += char 
print(newString)

# How to reverse the words in a string?
str = "Hello World"
wordList = str.split()
reversedWordList = []
for word in wordList:
    reversedWordList.append(word[::-1])
print(" ".join(reversedWordList))

# How to count the number of vowels in a string?
vowelsCount = 0
for char in str:
    vowels = "aeiou"
    if vowels.count(char) > 0:
        vowelsCount += vowels.count(char)
print(vowelsCount)

# How to convert a string to a list of characters?
charList = []
for char in str:
    charList.append(char)
print(charList)

# How to find the number of words in a string?
print(len(str.split()))

# How to convert a string to a list of words without spaces?
str = "   hello  world   "
print(str.split())

# How to capitalize the first letter of each sentence in a paragraph?
str = "hello world"
print(str.title())

# How to convert a string to a list of characters without duplicates?
wordList = []
for char in str:
    if char not in wordList:
        wordList.append(char) 

print(wordList)