#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError as e:
        print(f"Exception: {e}", file=stderr)
        return False
    except NameError as ne:
        print(f"Exception: {ne}", file=stderr)
        return False
