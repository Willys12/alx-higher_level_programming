#!/usr/bin/python3
def print_last_digit(number):
    while number > 9:
        number = number // 10
    print(number)
