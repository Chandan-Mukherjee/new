data = [5, 8, 4, 6, 9, 2]

value = 12

for i in data:
    if i == value:
        print(value, 'is found in ', data)
        print('index is: ',data.index(i))
        break
else:
    print(value, 'is not found in ',data)