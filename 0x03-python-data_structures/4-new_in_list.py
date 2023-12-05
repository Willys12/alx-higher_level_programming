#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:idx] + [element] + my_list[idx + 1:]

    if idx < 0 or idx >= len(new_list):
        return new_list
    return new_list
