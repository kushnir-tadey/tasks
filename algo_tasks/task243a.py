from math import *

"""243 a.) Given natural number n. Can we represent it as the sum of two squares of natural numbers?  
If possible, then find a pair x, y of such natural numbers that n = x^2 + y^2"""


def check_input(num):
    """Check the input"""
    while num.isalpha():
        num = input("n should be a number: ")

    num = int(num)

    while num < 1:
        num = int(input("Enter n again, should be > 0: "))

    return int(num)


def task243a():
    n = check_input(input("Enter n > 1: "))

    n_sqrt = sqrt(n)

    for y in range(1, int(n_sqrt) + 1):
        x = sqrt((n_sqrt + y) * (n_sqrt - y))

        if int(x) == x:
            if int(x) > 0:
                return f"Pair of x, y: {int(x), y}"

        elif abs(round(x) - x) < 0.0000000001:
            if round(x) > 0:
                return f"Pair of x, y: {round(x), y}"

    return "There is no pair of such x, y"


print(task243a())
