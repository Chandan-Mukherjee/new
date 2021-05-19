# Chapter 35 is important.

a = int(input("Put first number: "))
b = int(input("Put second number: "))

try:
    if b == 0:
        raise Exception('The denominator can not be zero.')
    print(a / b)
except Exception as e:
    print(e)


