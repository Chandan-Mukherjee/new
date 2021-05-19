class A:

    def __init__(self, par1):
        self.par1 = par1
        print('Hi')


class B:

    def __init__(self, par2, par3):
        self.par2 = par2
        self.par3 = par3
        print('Hey')


class C(A, B):

    def __init__(self):
        super().__init__('par1', 'par2')


c = C()

# in case of multiple inheritance , it will work as per MRO...


# super() is really super thing, by using this not only the constructors , we can also call the methods of it.

