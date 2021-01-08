# types of Arguments are: Positional, keyword, default, variable length

# this is an example of valriable length argument

# while args take one asterix , kwargs will tale two asterix

# video number 39 is important

def func(*a):
    sum = 0
    for i in a:
        sum += i
    return sum


print(func(1, 2, 3, 4,1))
