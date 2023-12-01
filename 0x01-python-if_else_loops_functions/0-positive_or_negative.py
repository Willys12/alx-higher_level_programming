#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# My statement
for i in range(-10, 10):
    if i < 0:
        print(f"{i} is negative")
    elif (i == 0):
        print(f"{i} is zero")
    else:
        print(f"{i}is positive")
print(f"{number}")