#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(num):
    return num % 10 if num >= 0 else -(-num % 10)


# Get last digit of number generated
ld = last_digit(number)


# Check if number is less than 5 & 6 and not 0
if ld > 5:
    print(f"Last digit of {number} is {ld} and is greater than 5")
elif ld == 0:
    print(f"Last digit of {number} is {ld} and is 0")
elif ld < 6 and ld < 0:
    print(f"Last digit of {number} is {ld} and is\
 less than 6 and not 0")
