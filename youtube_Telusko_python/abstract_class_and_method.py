from abc import abstractmethod, ABC


# abc module stands for 'Abstract Base Class'

class A(ABC):

    @abstractmethod
    def abstract_method(self):
        pass


class B(A):
    # pass

    def abcd(self):
        pass


b = B()


# The main thing about abstract class is that , the class that directly inherits the abstract class. we cannot create object of that class directly.
# abstrct class must have ateast one abstract method.

