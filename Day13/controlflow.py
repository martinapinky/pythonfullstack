# 1. Conditional statements

# if
x = 5
if x > 5:
    print("x is greater than 5")

# if else 
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")

# if elif else
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# for looping
for i in range(5):
    print(i)

# while
x = 0
while x < 5:
    print(x)
    x += 1

# break
for i in range(5):
    if i == 5:
        break
        print(i)

# pass
for i in range(5):
    if i == 2:
        pass  # placeholder for future logic
    print(i)

########### 2D array example
rows, col = 2, 3
array = [[i * j for j in range(col)] for i in range(rows)]
print(array)