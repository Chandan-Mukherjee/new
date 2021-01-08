class person:
    leg = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, second_object):
        if self.age == second_object.age:
            print("Same age")
            return True


ravi = person('Ravi', 28)
navin = person('Navin', 28)

ravi.leg = 3

print(ravi.leg)
print(navin.leg)


# Even if you change the class variable by using an instance , it will only be changed for that instance and not for that entire class.

