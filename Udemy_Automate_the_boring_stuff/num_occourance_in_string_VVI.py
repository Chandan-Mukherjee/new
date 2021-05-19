# This program is written to check the number of occourances of a letter in a string.

import pprint

string_name = 'Once upon a time, there was a little girl named Goldilocks. She went for a walk in the forest. Pretty soon, she came upon a house. She knocked and, when no one answered, she walked right in.'



count = {}

for letter in string_name.upper():
    count.setdefault(letter, 0)
    count[letter] += 1

pprint.pprint(count)
