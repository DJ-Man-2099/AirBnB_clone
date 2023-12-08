#!/usr/bin/python3
import re


def check_if_float(num):
    """
    check if string is a float
    """
    return re.match(r'^[-+]?[0-9]*\.[0-9]+$', num)
