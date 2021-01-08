class Student:

    def __init__(self, name='Name not provided', roll=0):
        self.name = name
        self.roll = roll
        # self.laptop = self.Laptop(make='make', model='model', price='price')

    def show(self):
        print(self.name)
        print(self.roll)
        # self.laptop.show()

    class Laptop:

        def __init__(self, make, model, price):
            self.make = make
            self.model = model
            self.price = price

        def show(self):
            print(self.make)
            print(self.model)
            print(self.price)


ajay = Student(name='Ajay Kamble', roll=21)
ajay.show()

ajay_laptop=Student.Laptop(make='Lenovo',model='i5',price=50000)
ajay_laptop.show()