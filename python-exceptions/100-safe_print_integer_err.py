#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        print(f"Exception: {(err.args[0])}", file=sys.stderr)
        return False
    except TypeError as err1:
        print(f"Exception: {(err1.args[0])}", file=sys.stderr)
        return False
