# chapter 30 is extremely important.
# chapter 32 is extremely important.
# chapter 33 is extremely important.

# to remove the confusion about operating system, we should join filepaths using os module.

# shutil module  : shell utility module is used for copying and moving of files.

# send2trash module

import os
import shutil

# print(os.path.join('folder1', 'folder2', 'folder3', 'abc.png'))

# in case if you want to know the separator your OS is using, you can check using

# print(os.sep)

# to get the current working directory

# print(os.getcwd())

# to get the absolute path of a file

# print(os.path.abspath('chapter1.py'))

# to check whether any path exists or not

# print(os.path.exists(
#     r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Udemy_Automate_the_boring_stuff\chapter1.py'))

# to get the size of a file

# print(os.path.getsize(r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Udemy_Automate_the_boring_stuff\chapter1.py'))

# to get the directories in a folder

# print(os.listdir(r'C:'))

# to create directories

# os.makedirs('dir')

# os.chdir(r'C:\Users\Chandan Mukherjee\Desktop\ALL_IN_DESKTOP')
#
# with open('automation_file.txt') as file:
#     print(file.readlines())


# VVI to remember: readlines gets the data in the form of strings inside a list.


# print(dir(shutil))


# shutil.copy(r"C:\Users\Chandan Mukherjee\Desktop\ALL_IN_DESKTOP\automation_file.txt",r'C:\Users\Chandan Mukherjee\Desktop')
# print('moved the files successfully.')


# copytree is used to copy entire folder with content.

# move is used to rename too

# for i in dir(os):
#     if not i.startswith('_'):
#         print(i)

# print(os.getcwd())

# for i in os.walk(r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Udemy_Automate_the_boring_stuff'):
#     print(i)

