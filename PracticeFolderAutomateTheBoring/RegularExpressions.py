import re

# for i in dir(re):
#     if not i.startswith('_'):
#         print(i, end=',  ')

regex = re.compile('%d%d')

string = 'test money heist is a very popular netflix original series 12.'

print(regex.findall(string))
