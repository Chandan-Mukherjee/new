z = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# this needs to be revised , I forgot this
from functools import reduce

# print(list(filter(lambda x: x % 2 == 0, z)))
# print(list(map(lambda x: x + 2, z)))
print((reduce((lambda x, y: x + y), z)))
