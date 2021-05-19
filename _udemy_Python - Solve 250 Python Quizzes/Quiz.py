# Swapping the cases of characters in a string

name = 'ChandaM'

print(name.swapcase())


# ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
#
#
#
# What is the result of max(ee_countries.values()) ?



#
# ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
# 
# 
# 
# What is an alternative way of removing a key-value pair by specifying the key, apart from using the del statement?

# pop



#
# ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
#
#
#
# How can you add multiple key-value pairs to the dictionary, at the same time (using a single line of code) ?
#
# Example: 'Latvia': '1.9M', 'Lithuania': '2.8M', 'Belarus': '9.4M'

# ee_countries.update([['Latvia': '1.9M'],[..




# ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
#
#
#
# What is the result of sorted(ee_countries.keys(), reverse = True)[1] ?
#
#


# ee_countries = {"Ukraine": "43.7M", "Russia": "143.8M", "Poland": "38.1M", "Romania": "19.5M", "Bulgaria": "6.9M", "Hungary": "9.6M", "Moldova": "4.1M", "Estonia": "1.3M"}
# 
# 
# 
# What is the result of sorted(ee_countries.values())[-2] ?



#
# >>> mylist = ['1.3M', '143.8M', '19.5M', '38.1M', '4.1M', '43.7M', '6.9M', '9.6M']
# >>> str(mylist)



# below are type conversions:


# What is the result of the code below?
#
# >>> int('a', 16)
#
#
#
# What is the result of the code below?
#
# >>> int('0011', 2)



# mydict = {1: "BTC", 2: "ETH", 3: "XRP", 4: "LTC", 5: "EOS", 6: "ADA", 7: "XLM"}
#
# print(type(list(mydict.items())[2]))



#
# True or false?
#
# In the case of a while loop, the indented code below the else clause will be executed only when the condition specified in the while statement becomes False.
#
#
#
# for i in range(1, 4):
#     for j in range(2, 4):
#         if j == 3:
#             continue
#         print(i * j)
#     print("Break or not?"
#




#     What is the
#     result
#     of
#     the
#     code
#     below?
#
#     def my_function(x, y, z):
#         sum = (x + y) * z
#         return
#
#
#     my_function(1, 4, 4)
#
#


#
# In the code below, *args is...
#
# def my_first_function(x, *args):


# ans: a tuple of arguments


# What is the
# result
# of
# the
# code
# below?
#
# def my_function():
#     print(var)
#     var = 10
#
#

# UnboundLocalError


# What is the
# result
# of
# the
# code
# below?
#
# var = 50
#
#
# def my_function():
#     print(var)
#     var = 10
#
#
# my_function()
#
# # my_function()





# What is the role of the x file access mode?

#Ans: you would use this mode for excludively creating the file. it fails and raises exception if the file exists.





# What does the truncate() method do in the code below?
#
# f = open("D:\\test.txt", "r+")
# f.truncate(7)
# f.close()


# ans: truncate() keeps the first 7 characters in the file and deletes the rest of them.




#
# What is the role of re.I in the code below?
#
# item = re.match("Dracula", mystr, re.I)

#ans: re.ID : statnds for ignore the case





# import re
#
# mystr = "Romania is the land of Dracula!"
#
# item = re.search("(.+?) is (.+?) Dracula", mystr)
#
# print(item.group())





# What is the role of the re.sub() method?

# ans: replaces all the occorances of the specified pattern in the target string with another string that you provided as an argument.




# How can you verify if MyNewClass() is indeed a child of MyClass() ?

#ans: issubclass(MyNewClass,MyClass)




# class MyClass(object):
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def print_e(self, e):
#         print("The result is: ", (self.a + e) * 10)
#
#
# class MyNewClass(MyClass):
#     def __init__(self, a, b, c, d, f):
#         MyClass.__init__(self, a, b, c, d)
#         self.f = f
#
#     def print_f(self, no):
#         print(self.f + no)
#
#
# y = MyNewClass(10, 20, 30, 40, 50)
#
# What is the
# result
# of
# getattr(y, "f") ?





result = list(filter((lambda a: a ** 2 + 1 <= 10), range(5)))
print(result)





# What is the exception raised when applying the next() function until the elements of mylist are exhausted?

#ans: stopiteration error



