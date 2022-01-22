class MyClass:
    description="an easy example"
    num=12345
    def func(self):
        print("hello world")

x=MyClass()
print(x.description)
print(x.num)
x.func()

# Every class own a default constructor
# like: def __init__(self)
# And all functions of one class must have a parameter "self"(can be other name) which must be the first in the parameter list

class Complex:
    def __init__(self,realpart,imagpart):
        self.i=realpart
        self.j=imagpart
    def Print(self):
        print("{0}+{1}j".format(self.i,self.j))

Complex(5,6).Print()

# inhetitance
class people:
    def __init__(self,Age,Name):
        self.age=Age
        self.name=Name
    def Show(self):
        print("Age : {0}   Name : {1}".format(self.age,self.name))

class student(people):
    def __init__(self,Age,Name,Grade):
        people.__init__(self,Age,Name)
        self.grade=Grade
    def Show(self):
        print("Age : {0}   Name : {1}   Grade : {2}".format(self.age,self.name,self.grade))

people(20,'John').Show()
student(16,"David","senior school").Show()













