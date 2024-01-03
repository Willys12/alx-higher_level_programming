#!/usr/bin/python3
def print_last_digit(number):
    num_str = str(abs(number))
    if num_str[-1] == '0':
        return int(num_str)
    else:
        return int(num_str[-1])
