# Python中可以使用内置方法isinstance()来测试一个对象是否为某个类的实例
class Car:
    pass

car=Car()
print(isinstance(car,Car))
car=123
print(isinstance(car,Car))

# 类的所有实例方法都必须至少有一个名为self的参数，且必须是方法的第一个形参（如果有多个形参的话），self参数代表将来要创建的对象本身。
# 在类的实例方法中访问实例属性时需以self为前缀。
# 在外部通过对象调用对象方法时并不需要传递这个参数，如果在外部通过类调用对象方法则需要显式为self参数传值。
# 在类中定义实例方法时将第一个参数定义为“self”只是一个习惯，虽不必须使用，仍建议编写代码时仍以self作为方法的第一个参数名字。
# 属于实例的数据成员一般是指在构造函数__init__()中定义的，定义和使用时必须以self作为前缀；
# 属于类的数据成员是在类中所有方法之外定义的。
# 在主程序中（或类的外部），实例属性属于实例(对象)，只能通过对象名访问；而类属性属于类，可以通过类名或对象名都可以访问。
# 在实例方法中可以调用该实例的其他方法，也可以访问类属性以及实例属性。

class Car:
    price=0
    # self.test='test'
    def __init__(self,c):
        self.color=c

car=Car('red')
print(car.color)
print(car.price)
print(Car.price)
Car.test='test'#动态增加类属性
print(car.test)
car._test='test'
print(car._test)
import types

car.setSpeed=types.MethodType(lambda self,x:print(x+10),car)#self不可少 动态增加成员方法
car.setSpeed(100)

# 在Python中，函数和方法是有区别的。
# 方法一般指与特定实例绑定的函数，通过对象调用方法时，对象本身将被作为第一个参数隐式传递过去，普通函数并不具备这个特点。

# Python并没有对私有成员提供严格的访问保护机制。
# 在定义类的成员时，如果成员名以两个下划线“__”或更多下划线开头而不以两个或更多下划线结束则表示是私有成员。
# 私有成员在类的外部不能直接访问，需要通过调用对象的公开成员方法来访问，也可以通过Python支持的特殊方式来访问。

class A:
    def __init__(self):
        self.__private='private'
        self.public='public'
    def Private(self):
        print(self.__private)
    def __Private(self):
        print(self.public,self.__private)

print(A().public)
A().Private()
# A().__Private()

# Python中以下划线开头的变量名和方法名有特殊含义，尤其是在类的定义中。
# _xxx：受保护成员，不能用'from module import *'导入；
# __xxx__：系统定义的特殊成员；
# __xxx：私有成员，只有类对象自己能访问，子类对象不能直接访问到这个成员，
# 但在对象外部可以通过“对象名._类名__xxx”这样的特殊方式来访问。
# 注意：Python中不存在严格意义上的私有成员。
print(A()._A__private)

# 在程序中，可以使用一个下划线来表示不关心该变量的值
for _ in range(1):
    print('test')
print('--------------------------------------------------------------------')

# 私有方法的名字以两个下划线“__”开始，每个对象都有自己的公有方法和私有方法，在这两类方法中可以访问属于类和对象的成员；
# 公有方法通过对象名直接调用，私有方法不能通过对象名直接调用，
# 只能在属于对象的方法中通过self调用或在外部通过Python支持的特殊方式来调用。
# 如果通过类名来调用属于对象的公有方法，需要显式为该方法的self参数传递一个对象名，用来明确指定访问哪个对象的数据成员。

# 静态方法和类方法都可以通过类名和对象名调用，但不能直接访问属于对象的成员，只能访问属于类的成员。
# 静态方法可以没有参数。
# 一般将cls作为类方法的第一个参数名称，但也可以使用其他的名字作为参数，并且在调用类方法时不需要为该参数传递值。
class Root:
    __total = 0
    def __init__(self, v):    #构造方法
        self.__value = v
        Root.__total += 1

    def show(self):           #普通实例方法
        print('self.__value:', self.__value)
        print('Root.__total:', Root.__total)

    @classmethod              #修饰器，声明类方法
    def classShowTotal(cls):  #类方法
        print(cls.__total)

    @staticmethod             #修饰器，声明静态方法
    def staticShowTotal():    #静态方法
        print(Root.__total)

Root.staticShowTotal()
# Root.show()
Root.show(Root(5))
Root.classShowTotal()
print('--------------------------------------------------------------------')
# Python中类的构造函数是__init__()，一般用来为数据成员设置初值或进行其他必要的初始化工作，
# 在创建对象时被自动调用和执行。如果用户没有设计构造函数，Python将提供一个默认的构造函数用来进行必要的初始化工作。
# Python中类的析构函数是__del__()，一般用来释放对象占用的资源，在Python删除对象
# 和收回对象空间时被自动调用和执行。如果用户没有编写析构函数，Python将提供一个默认的析构函数进行必要的清理工作。

# 只读属性
class Test:
	def __init__(self, value):
	    self.__value = value

	@property
	def value(self):               #只读，无法修改和删除
	    return self.__value

test=Test(10)
print(test.value)
# test.value=5
# del test.value
# 可读、可写属性
class Test:
	def __init__(self, value):
		self.__value = value

	def __get(self):
		return self.__value

	def __set(self, v):
		self.__value = v

	value = property(__get, __set)

	def show(self):
		print(self.__value)
test=Test(5)
print(test.value)
test.value=10
test.show()

# 可读、可修改、可删除的属性。
class Test:
	def __init__(self, value):
		self.__value = value

	def __get(self):
		return self.__value

	def __set(self, v):
		self.__value = v

	def __del(self):
		del self.__value

	value = property(__get, __set, __del)

	def show(self):
		print(self.__value)
print('--------------------------------------------------------------------')

# 在继承关系中，已有的、设计好的类称为父类或基类，新设计的类称为子类或派生类。
# 派生类可以继承父类的公有成员，但是不能继承其私有成员。如果需要在派生类中调用基类的方法，
# 可以使用内置函数super()或者通过“基类名.方法名()”的方式来实现这一目的。
class A(object):
    def __init__(self):  # 构造方法可能会被派生类继承
        self.__private()
        self.public()#如果子类有同名的方法将其覆盖，则调用子类的方法

    def __private(self):  # 私有方法在派生类中不能直接访问
        print('__private() method in A')

    def public(self):  # 公开方法在派生类中可以直接访问，也可以被覆盖
        print('public() method in A')


class B(A):  # 类B没有构造方法，会继承基类的构造方法

    def __private(self):  # 这不会覆盖基类的私有方法
        print('__private() method in B')

    def public(self):  # 覆盖了继承自A类的公开方法public
        print('public() method in B')
        super().public()

b=B()
b.public()
class C(B):
    def __init__(self):
        self.__private()
        super().public()

    def __private(self):
        print('private in C')

c=C()
# 如果父类中有相同的方法名，而在子类中使用时没有指定父类名，则Python解释器将从左向右按顺序进行搜索。
# 在Python 3.x的多继承树中，如果在中间层某类有向上一层解析的迹象，
# 则会先把本层右侧的其他类方法解析完，然后从本层最后一个解析的类方法中直接进入上一层并继续解析，
# 也就是在从子类到超类的反向树中按广度优先解析。
# 如果在解析过程中，不再有向基类方向上一层解析的迹象，则同一层中右侧其他类方法不再解析。
print('---------------------------------------------------------------------------')
class Animal(object):      #定义基类
    def show(self):
        print('I am an animal.')
class Cat(Animal):         #派生类，覆盖了基类的show()方法
    def show(self):
        print('I am a cat.')
class Dog(Animal):         #派生类
    def show(self):
        print('I am a dog.')
class Tiger(Animal):       #派生类
    def show(self):
        print('I am a tiger.')
class Test(Animal):        #派生类，没有覆盖基类的show()方法
    pass
x = [item() for item in (Animal, Cat, Dog, Tiger, Test)]
for item in x:
    item.show()



