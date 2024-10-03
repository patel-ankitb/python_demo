# enculation -------------->

'''class Example:
    data = "date1"
    _data = "date2"
    __data = "date3"

    def dispaly(self):
        print(self.data)
        print(self._data)
        print(self.__data)
# class Example2(Example):
#     def display(self):
#         print(self.data)
#         print(self._data)
#         print(self.__data)

obj = Example()
obj.dispaly()'''


# abstraction ----------------->

from abc import ABC ,abstractmethod
class AbstractClass(ABC):
    def dis(self):
        pass
    @abstractmethod
    def display(self):
        pass
class ChildClass(AbstractClass):
    def display(self):
        pass

obj = ChildClass()
