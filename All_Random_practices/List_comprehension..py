a = range(0,100,2)
print(list(a))

print(list(i*i for i in list(a)))


###

a = list(range(1, 101))

for i in a:
    if i % 3 != 0 or i % 5 != 0:
        print(i)

print(list((i for i in a if i % 3 != 0 or i % 5 != 0)))
