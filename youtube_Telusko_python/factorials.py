import math

print(math.factorial(10))


def fact(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


print(fact(10))


def fact1(n):
    if n == 0:
        return 1
    return n * fact1(n - 1)


print(fact1(10))
