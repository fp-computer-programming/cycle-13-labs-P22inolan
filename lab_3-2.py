# Author: IBN AMDG (3/7/2022)

from functools import total_ordering


def factorial(element):
    total = 1
    x  = 1
    if element != 0:
        while x <= element:
            total *= x
            x += 1
    elif element == 0:
        print("0 does not have a factorial.")
    return total

