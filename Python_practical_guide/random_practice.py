a = []
a1 = []
a1 += a


def blockchain():
    value = input('Enter the value: ')
    if value != '':
        a.append(value)


for i in range(3):
    blockchain()
    print(a1)
