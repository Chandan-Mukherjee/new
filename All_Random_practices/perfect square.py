# perfect squares between 1 to 500

import math

for i in range(500):
    z = math.sqrt(i)
    if z - math.floor(z) == 0.0:
        print(i, 'is a perfect square number.')
