# name = 'youtube'
# # what will this print ? name[8]
#
# # the error name while trying to change a string
#
# # VVI the difference between append and extend.
#
# names = ['chandan', 'anil', 'badal', 'pallab']
# names.append('abcd')
# print(names)
# names.extend('def')
# print(names)
#
# # in extend you need to put the values always in the list form or in some form that can be directly converted in list.
#
# # converting a set to a sorted set
# a = {1, 3, 4, 7, 2, 6}
# print(set(sorted(a)))
#
# # what error does a dictionary give if a key is not present there.
# # get and set methods of dictionary and need of that.
# # also know the meaning of getdefault and setdefault
#
# # dict.get(1,'not found')

keys = [1, 2, 3]
values = ['python', 'java', 'JS']

# VVI : zip function

data = dict(zip(keys, values))
print(data)

data[4] = 'c#'
print(data)

del(data[1])
print(data)

# in the python help prompt if we mention 'topics' then it will show all the commands for help.

# list(range(0,10,2))

# number type conversion: bin, dec, oct , hex

# >>> 25
# 25
# >>> bin(25)
# '0b11001'
# >>>
# >>> hex(25)
# '0x19'
# >>>
# >>> oct(25)
# '0o31'
# >>>


# Swapping of numbers:

# >>>
# >>> a=5
# >>> b=2
# >>>
# >>> a,b=b,a
# >>> a
# 2
# >>> b
# 5
# >>> a=a+b
# >>> b=a-b
# >>> a=a-b
# >>> a
# 5
# >>> b
# 2
# >>> a=a^b
# >>> b=a^b
# >>> a=a^b
# >>> a
# 2
# >>> b
# 5
# >>>


# bitwise operators ( ~ - compliment , & - and , | - or , ^ - xor, << - left shft , >> -right shift )
# 12 & 13

# Binary operators video is important from telusko videos.


# IMP: When you import a module by alias name, then the module real name as well as alias name both will work.

# eval function : This will evaluate the data from input

# chapter 21 on user input is extremely important, mainly command line input from user. --------------------------------------------




