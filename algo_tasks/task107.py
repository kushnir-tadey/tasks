from math import log

"""107. Given integer m > 1. Find the greatest integer k, that inequality 4^k < m is right."""


def check_input(num):
    """Check the input"""
    while num.isalpha():
        num = input("n should be a number: ")

    num = int(num)

    while num <= 1:
        num = int(input("Enter n again, should be > 1: "))

    return int(num)


def task107():
    m = check_input(input("Enter m > 1: "))

    k = int(log(m, 4))

    if pow(4, k) == m:
        k -= 1

    return f"k = {k}, (4^{k} < {m})"


print(task107())
