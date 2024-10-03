'''class MyClass:
    a=10
    def Method(self,a):
        self.a =22
        print(a)
        print(self.a)
x=MyClass()
print(x.Method(99))'''

'''
class MyClass:
    dic={
        '1':'ankit',
        '2':'yash',
        '3':'jay'
    }
    def method(self,d):
          self.dic
          print(self.dic.get(d))
x=MyClass()
print(x.method((input("enter the roll-number = "))))'''

'''class StdDetails:
    name = {1:'abc',2:'xyz',3:'pqr'}
    position = {1:2,2:1,3:3}
    def search(self,y):
        print(self.name[y],' - ',self.position[y])

a = StdDetails()
a.search(2)'''

class MyClass:
    def __init__(self,rno,name,std):
        print("init")
        self.rno=rno
        self.name=name
        self.std=12
a=MyClass(1,'ankit',12)
print(a)