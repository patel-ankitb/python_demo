from abc import ABC ,abstractmethod
class Parent(ABC):
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
class Child(Parent):
    def m2(self):
        print("m.2")
    def display(self):
        print("c.display")
ch = Child()
ch.display()
