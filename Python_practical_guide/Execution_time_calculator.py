import time


def time_calculator():
    print(f'current time is {time.ctime()}')
    time.sleep(20)
    print('waited for 20 seconds')


print('Program is started, function is called now')
a = time.ctime()
time_calculator()
print(f'Program is stopped, excuted the function and current time is {time.ctime()}')
b = time.ctime()
# print(f' Total time taken for execution is {}')
