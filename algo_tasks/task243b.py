from math import *

"""243 b.) Given natural number n. Can we represent it as the sum of two squares of natural numbers?  
If possible, then find all pairs x, y of such natural numbers that n = x^2 + y^2, x >= y."""


def check_input(num):
    """Check the input"""
    while num.isalpha():
        num = input("n should be a number: ")

    num = int(num)

    while num < 1:
        num = int(input("Enter n again, should be > 0: "))

    return int(num)


def task243b():
    n = check_input(input("Enter n > 1: "))

    n_sqrt = sqrt(n)

    squares = []

    for y in range(1, int(n_sqrt) + 1):
        x = sqrt((n_sqrt + y) * (n_sqrt - y))

        if int(x) == x:
            if int(x) >= y:
                squares.append((int(x), y))

        elif abs(round(x) - x) < 0.0000000001:
            if round(x) >= y:
                squares.append((round(x), y))

    if len(squares) == 0:
        return "There is no pairs of such x, y"

    return f"Pair(s) of x,y: {squares}"


print(task243b())