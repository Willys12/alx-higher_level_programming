#!/usr/bin/env python3
def print_list_integer(my_list=[]):
    new_list = my_list[:]

    for element in new_list:
        print("{}".format(element))
