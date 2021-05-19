#  a generator is a function that returns an object (iterator) which we can iterate over (one value at a time)..

# important video, Telusko

def it():
    for i in range(1, 11):
        yield i * i


for i in it():
    print(i)

