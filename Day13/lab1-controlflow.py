# 1. Find numbers divisible by 7 and multiples of 5 between 1500 and 2700
print([i for i in range(1500, 2700) if i % 7 == 0 and i % 5 == 0])

# 2. Convert temperatures between Celsius and Fahrenheit
def convert_temperature(temp, unit):
    if unit == 'C':
        return f"{temp}C is {(temp * (9 / 5)) + 32}F"
    elif unit == 'F':
        return f"{temp}F is {(temp - 32) * (5 / 9)}C"
    else:
        return "Unknown temperature unit" 

print(convert_temperature(60, 'C'))

# 3. Guess a number between 1 and 9
import random
def guess_number():
    number = random.randint(1, 9)
    n = int(input("Guess a number between 1 and 9: "))
    if n == number:
        return print("Well guessed!")
    else:
        guess_number()

# guess_number()

# 4. Print pattern using nested loops
def print_pattern():
    for i in range(1, 6):
        print("* " * i)
    for i in range(4, 0, -1):
        print("* " * i)

print_pattern()

# 5. Reverse a word entered by the user
def reverse_word():
    word = input("Enter a word: ")
    return word[::-1]

# print(reverse_word())

# 6. Count even and odd numbers in a tuple
def count_even_odd(my_tuple):
    count_dictionary = {}
    for value in my_tuple:
        if value % 2 == 0:
            count_dictionary['even'] = count_dictionary.get('even', 0) + 1
        else:
            count_dictionary['odd'] = count_dictionary.get('odd', 0) + 1
    return count_dictionary

print(count_even_odd((1, 2, 3, 4, 5, 6, 7, 8, 9)))

# 7. Print items and their types from a list
def print_types(lst):
    for element in lst:
        print(element, type(element))

print_types([1, 2.5, "Hello", False])

# 8. Print numbers from 0 to 6 except 3 and 6
for i in range(0, 6):
    if i == 3:
        pass
    else:
        print(i)

# 9. Fibonacci series between 0 and 50
n = 50
a, b = 0, 1
print("Fibonacci series >>>>>>>>>>>")
print(a)
print(b)
for i in range(2, n):
    c = a + b
    if c > 50:
        break
    print(c)
    a = b
    b = c

# const n = 10;
# let a = 0, b = 1;
# console.log(a);
# console.log(b);
# for(let i = 2; i < n; i++) {
#     const c = a + b;
#     console.log(c);
#     a = b;
#     b = c;
# }

# 10. Print FizzBuzz for numbers 1 to 50
print("FizzBuzz for numbers 1 to 50")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)

# 11. Generate 2D array with i*j values
rows, cols = 2, 3
print([[i * j for i in range(cols)] for j in range(rows)])

# 12. Accept sequence of lines and convert to lowercase
multiline_string = """LOREM
IPSUM
DOLOR"""
def to_lower(str1):
    return str1.lower()

print(to_lower(multiline_string))

################################ Filter 4-digit binary numbers divisible by 5

# 13. Count letters and digits in a string
def count_letters_digits(strmixed):
    count_dictionary = {}
    for char in strmixed:
        if char.isdigit():
            count_dictionary['digits'] = count_dictionary.get('digits', 0) + 1
        elif char.isalpha():
            count_dictionary['letters'] = count_dictionary.get('letters', 0) + 1
        else:
            pass
    return count_dictionary

print(count_letters_digits("Hello123!"))

################################### Validate password based on given conditions

# 14. Find numbers where each digit is even (100-400)
print([i for i in range(100, 400) if all(int(digit) % 2 == 0 for digit in str(i))])

# 15. Write a Python program to calculate a dog's age in dog years.
def calculate_dog_years(human_years):
    if human_years < 3:
        return human_years * 10.5
    else:
        return 21 + (human_years - 2) * 4

print(calculate_dog_years(4))

# 16. Write a Python program to check whether an alphabet is a vowel or consonant.
def is_vowel_or_consonant(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char in vowels or char in [v.upper() for v in vowels]:
        return f"{char} is a vowel"
    else:
        return f"{char} is a consonant"

print(is_vowel_or_consonant('B'))

# 17. Write a Python program to convert a month name to a number of days.
def month_days_number(month, is_leap_year=False):
    if month in ['September', 'April', 'June', 'November']:
        return 30
    elif month == 'February' and is_leap_year:
        return 29
    elif month == 'February' and not is_leap_year:
        return 28
    else:
        return 31

print(month_days_number('February', True))

# 18. Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.
def sum_two_integers(a, b):
    return 20 if a + b > 15 and a + b < 20 else a + b 

print(sum_two_integers(10, 6))

# 19. Write a Python program that checks whether a string represents an integer or not.
def is_integer(string):
    return string.isdigit()

print(is_integer('32'))

# 20. Write a Python program to check if a triangle is equilateral, isosceles or scalene.
def check_triangle(a, b, c):
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c:
        return "Isoceles triangle"
    else:
        return "Scalene tiangle"
    
print(check_triangle(2, 3, 2))

# 21. Write a Python program that reads two integers representing a month and day and prints 
# the season.

def find_season(month, day):
    seasons = {
        "Spring": [("March", 21), ("June", 21)],  
        "Summer": [("June", 21), ("September", 23)],
        "Autumn": [("September", 23), ("November", 21)],
        "Winter": [("November", 21), ("March", 21)]  
    }
   
    months_in_order = ["January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November", "December"]
   
    for season, dates in seasons.items():
        start_month, start_day = dates[0]  
        end_month, end_day = dates[1]  

        if months_in_order.index(month) >= months_in_order.index(start_month) and \
           (month != end_month or day < end_day):
            return season
    return "Invalid day or month"

# month_input = input("Input the month ")  # Output: "June"
# day_input = int(input("Input the day (1-31): "))  # Output: 22

# season = find_season(month_input, day_input)
# print(f"The season is {season}.")  # Example output: "The season is Spring."

# 22. Write a Python program to display the astrological sign for a given date of birth.
def astrological_sign(month, day):
    sign_dates = {
        "Aries": [("March", 21), ("April", 19)],
        "Taurus": [("April", 20), ("May", 20)],
        "Gemini": [("May", 21), ("June", 21)],
        "Cancer": [("June", 22), ("July", 22)],
        "Leo": [("July", 23), ("August", 22)],
        "Virgo": [("August", 23), ("September", 22)],
        "Libra": [("September", 23), ("October", 23)],
        "Scorpio": [("October", 24), ("November", 21)],
        "Sagittarius": [("November", 22), ("December", 21)],
        "Capricorn": [("December", 22), ("January", 19)],
        "Aquarius": [("January", 20), ("February", 18)],
        "Pisces": [("February", 19), ("March", 20)]
    }

    months_in_order = ["January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November", "December"]
    
    for sign, dates in sign_dates.items():
        start_month, start_day = dates[0]  
        end_month, end_day = dates[1]

        if (months_in_order.index(month) >= months_in_order.index(start_month) and \
            months_in_order.index(month) <= months_in_order.index(end_month)) and \
           ((month == end_month and day <= end_day) or (month == start_month and day >= start_day)):
            return sign
        
    return "Invalid day or month"

month_input = input("Input the month: ")  # Output: "June"
day_input = int(input("Input the day (1-31): "))  # Output: 22

sign = astrological_sign(month_input, day_input)
print(f"The sign is {sign}.")  # Example output: "The sign is Gemini."

