# please note the number type error I did not intentionally handled , so make sure to enter number only
# also for loop related cases I have using 'for' loop only , while loop also can be done.

# procedure 1 (Error not handled)
from math import factorial

print(f'\nThe factorial of the entered number is {factorial(int(input("please enter the number:")))}')


# using recursion
def factorial_number(fact):
    if fact == 0:
        return 1
    else:
        return fact * factorial_number(fact - 1)


print(factorial_number(int(input('Please enter the number:'))))


# using for loop
def factorial_using_loop():
    fact = 1
    num = int(input('please enter the number:'))
    if num == 0:
        return 1
    else:
        for i in range(num, 0, -1):
            fact *= i
        return fact


print(factorial_using_loop())
