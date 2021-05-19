class A:

    def methodA(self):
        pass

    def methodB(self, par1):
        pass


class B(A):

    def methodC(self):
        pass

    def methodA(self):
        pass


# The drawback of method overloading is removed by either default parameters or args and kwargs.

