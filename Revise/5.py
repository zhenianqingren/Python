# 生成斐波那契数列的函数定义和调用
def fib(n):
    a,b=1,1
    while a<n:
        print(a)
        a,b=b,a+b
fib(100)
# Python中的函数和自定义对象的成员也是可以随时发生改变的，可以为函数和自定义对象动态增加新成员。
def func():
    print()
func.x=5
print(func.x)
# del func().x
# print(func().x)
# 函数定义时括弧内为形参，一个函数可以没有形参，但是括弧必须要有，表示该函数不接受参数。
# 函数调用时向其传递实参，将实参引用传递给形参。
# 在定义函数时，对参数个数并没有限制，如果有多个形参，需要使用逗号进行分隔。
# 对于绝大多数情况下，在函数内部直接修改形参的值不会影响实参，而是创建一个新变量。
def addOne(a):
    print(id(a),a)
    a=a+1
    print(id(a),a)

a=1
print(id(a),a)
addOne(a)
# 有些情况下，可以通过特殊的方式在函数内部修改实参的值。
def modify(v):
    v[0]=v[0]+1
v=[1]
modify(v)
print(v)
# 如果传递给函数的实参是可变序列，并且在函数内部使用下标或可变序列自身的方法增加、删除元素或修改元素时，实参也得到相应的修改。
# 在Python中，函数参数有很多种：可以为普通参数、默认值参数、关键参数、可变长度参数等等。
# Python在定义函数时不需要指定形参的类型，完全由调用者传递的实参类型以及Python解释器的理解和推断来决定，类似于重载和泛型。
# 位置参数（positional arguments）是比较常用的形式，调用函数时实参和形参的顺序必须严格一致，并且实参和形参的数量必须相同。
def demo1(a,b,c):
    print(a,b,c)
demo1(1,2,3)
demo1(2,3,1)
# demo1(1,2,3,4)
print('----------------------------------------------------------------------')
# 一年365天，以第1天的能力值为基数，记为1.0，当好好学习时能力值相比前一天提高r‰，
# 当没有学习时由于遗忘等原因能力值相比前一天下降r‰。每天努力和每天放任，一年下来的能力值相差多少呢？
def DayUpAndDown(r):
    dayup=pow((1.0+r),365)
    daydown=pow((1.0-r),365)
    return dayup,daydown
u,d=DayUpAndDown(0.1)
print(u,d,sep='     ')
print('----------------------------------------------------------------------')
# 调用带有默认值参数的函数时，可以不对默认值参数进行赋值，也可以为其赋值，具有很大的灵活性。
def say(message,times=1):
    print(message*times)
say('fuck')
say('fuck',10)
# 注意：默认值参数必须出现在函数参数列表的最右端，任何一个默认值参数右边不能有非默认值参数。
def Join(List,sep=None):
    return (sep or '').join(List)
aList = ['a', 'b', 'c']
print(Join(aList))
print(Join(aList,','))
print('----------------------------------------------------------------------')
# 另外，默认值参数如果使用不当，会导致很难发现的逻辑错误
def demo2(newitem,old_list=[]):
    old_list.append(newitem)
    return old_list
print(demo2('5',[1,2,3,4]))
print(demo2('aaa',['a','b']))
print(demo2('a'))
print(demo2.__defaults__)
print(demo2('b'))
# 可以使用“函数名.__defaults__”查看所有默认参数的当前值
def demo(newitem,old_list=None):
    if old_list == None:
        old_list=[]
    new_list = old_list[:]
    new_list.append(newitem)
    return new_list
# 默认值参数只在函数定义时被解释一次

print(demo('5',[1,2,3,4]))
print(demo('aaa',['a','b']))
print(demo('a'))
print(demo.__defaults__)
print(demo('b'))
print()
old_list=['a']
new_list=old_list[:]
new_list.append('b')
print(new_list)
print('----------------------------------------------------------------------')

# 通过关键参数，实参顺序可以和形参顺序不一致，但不影响传递结果，避免了用户需要牢记位置参数顺序的麻烦。
def demo(a,b,c):
    print(a,b,c)
demo(1,2,3)
demo(2,1,3)
demo(b=2,a=1,c=3)
# 可变长度参数
# 可变长度参数主要有两种形式：在参数名前加1个*或2个**
# *parameter用来接收多个位置实参并将其放在一个元组中
# **parameter接收多个关键参数并存放到字典中
def demo(*p):
    print(p)

demo(1,2,3,4)
def demo_(**p):
    print(p)
demo_(x=1,y=2,z=3)
# demo_(1,2,3)
print('----------------------------------------------------------------------')
# 参数传递的序列解包
# 传递参数时，可以通过在实参序列前加一个星号将其解包，然后传递给多个单变量形参。
def _demo(a, b, c):
    print(a+b+c)
seq=[1,2,3]
tup=(1,2,3)
dic={1:'a',2:'b',3:'c'}
se={1,2,3}
_demo(*seq)
_demo(*tup)
_demo(*se)
_demo(*dic)
_demo(*dic.values())
# 如果函数实参是字典，可以在前面加两个星号进行解包，等价于关键参数。
def Demo(a,b,c):
    print(c,b,a)
dic={'a':1,'b':2,'c':3}
Demo(**dic)
# 调用函数时对实参序列使用一个星号*进行解包后的实参将会被
# 当做普通位置参数对待；
# 且会在关键参数和使用两个星号**进行序列解包的参数之前
# 进行处理。
# demo(a=1, *(2, 3))
# demo(**{'a':1, 'b':2}, *(3,))  序列解包不能在关键参数解包之后
# demo(*(3,), **{'a':1, 'b':2})  序列解包放在关键参数解包之前，但a被多次赋值

print('----------------------------------------------------------------------')
# 变量起作用的代码范围称为变量
# 的作用域，不同作用域内变量名
# 可以相同，互不影响。
# 在函数内部定义的普通变量只在
# 函数内部起作用，称为局部变量。
# 当函数执行结束后，局部变量自动删除，不再可以使用。
# 局部变量的引用比全局变量速度快，应优先考虑使用。
# 全局变量可以通过关键字global来定义。这分为两种情况：
# 一个变量已在函数外定义，如果在函数内需要为这个变量赋值，并要将这个赋值结果反映到函数外，可以在函数内使用global将其声明为全局变量。
# 如果一个变量在函数外没有定义，在函数内部也可以直接将一个变量定义为全局变量，该函数执行后，将增加一个新的全局变量。
x=5
def test1():
    global x
    global y
    y=3
    print(x,y)

test1()
print(x,y)

a=1
def test2():
    global a
    print(a)
    a=2
    print(a)
test2()
print(a)

# 注意：在某个作用域内任意位置只要有为变量赋值的操作，该变量在这个作用域内就是局部变量，除非使用global进行了声明。
global t
t='test'
def func():
    print(t)
func()
# 如果局部变量与全局变量具有相同的名字，那么该局部变量会在自己的作用域内隐藏同名的全局变量。
# Python还支持使用nonlocal关键字定义一种介于二者之间的变量。关键字nonlocal声明的变量会引用距离最近的非全局作用域的变量，
# 要求声明的变量已经存在，关键字nonlocal不会创建新变量。
print('----------------------------------------------------------------------')
import random
x=[[random.randint(1,21) for j in range(5)] for i in range(5)]
for li in x:
    print(li)
print()
y=sorted(x,key=lambda item:(item[1],item[4]))#按子列表中第2个元素升序、第5个元素升序排序
for li in y:
    print(li)
print('----------------------------------------------------------------------')
# 编写函数计算圆的面积
from math import pi as PI
def CirCleArea(r):
    if isinstance(r,(int,float)) and r>0:
        return PI*r*r
    else:
        print('Wrong')
# 编写函数，接收包含20个整数的列表lst和一个整数k作为参数，返回
# 新列表。处理规则为：将列表lst中下标k之前的元素逆序，下标k之后
# 的元素逆序，然后将整个列表lst中的所有元素再逆序。
def Func(lst,k):
    m=lst[:k]
    m.reverse()
    n=lst[k:]
    n.reverse()
    m.extend(n)
    m.reverse()
    return m
te=list(range(1,21))
print(Func(te,8))
print('----------------------------------------------------------------------')
# 内置函数map()可以将一个函数作用到一个序列或迭代器对象上
average=list(map(lambda x:sum(x)/len(x),[[1,2,3],[4,5,6],[7,8,9]]))
print(average)
# 内置函数filter将一个函数作用到一个序列上，返回该序列中使得该函数返回值为True的那些元素组成的filter对象。
import string
strlist=list(filter(lambda x:len(x)==9,[''.join([random.choice(string.ascii_letters+string.digits) for j in range(random.randint(5,100))]) for i in range(200)]))
print(strlist)
# 标准库functools中的reduce()函数可以将一个接受2个参数的函数以迭代的方式从左到右依次作用到一个序列或迭代器对象的所有元素上。
from functools import reduce
seq=[1,2,3,4,5,6,7,8,9]
print(reduce(lambda x,y:x+y, seq))
# 生成器函数
# 包含yield语句的函数可以用来创建生成器对象，这样的函数也称生成器函数。
# 每次执行到yield语句会返回一个值然后暂停或挂起后面代码的执行，
# 下次通过生成器对象的__next__()方法、内置函数next()、for循环遍历生成器对象元素或其他方式显式“索要”数据时恢复执行。
# 生成器对象具有惰性求值的特点，适合大数据处理。

def f():
    a, b = 1, 1            #序列解包，同时为多个元素赋值
    while True:
        yield a            #暂停执行，需要时再产生一个新元素
        a, b = b, a+b      #序列解包，继续生成新元素
a = f()                #创建生成器对象
for i in range(10):    #斐波那契数列中前10个元素
    print(a.__next__(), end=' ')
# 函数嵌套定义
# 在Python中，函数是可以嵌套定义的。
def myMap(iterable, op, value):      #自定义函数
    if op not in '+-*/':
        return 'Error operator'
    def nested(item):                    #嵌套定义函数
        return eval(repr(item)+op+repr(value))
    return map(nested, iterable)         #使用在函数内部定义的函数
print()
print(list(myMap(range(5), '+', 5)))        #调用外部函数

def linear(a, b):
    def result(x):
        return a * x + b
    return result
taxes=linear(0.3,2)
print(taxes(5))












