from functools import reduce

def demo(new_item,old_list=[]):
    old_list.append(new_item)
    return old_list
print(demo('5',[1,2,3,4]))
print(demo('aaa',['a','b']))
print(demo('a'))
print(demo('b'))
# 默认值参数只在函数定义时被解释一次

def demo(a,b,c=5):
    print('a={}  b={}  c={}'.format(a,b,c))

# 关键参数
demo(1,2)
demo(1,2,3)
demo(2,1,3)
demo(b=2,a=1,c=3)

# 可变长度参数
def demo(*parameter):
    print(parameter[1])
    print(parameter)
    print(type(parameter))

demo(1,2,3,4,5,6,7)
print('-------------')
def demo_(**parameter):
    print(type(parameter))
    for item in parameter.items():
        print(item)

demo_(x=1,y=2,z=3)
# 关键参数解包
print('----------------')
def demo(x,y,z):
    print(x+y+z)
ls=[1,2,3]
demo(*ls)
tup=(1,2,3)
demo(*tup)
# 参数序列解包

def demo(a,b,c):
    print('a={}  b={}  c={}'.format(a,b,c))

dic={1:'a',2:'b',3:'c'}
print('----------')
print(dic.items())
print('-----------')
dicc={'a':1,'b':2,'c':3}# 关键参数解包
dicc={'x':1,'b':2,'c':3}# wrong
demo(*dic)
# demo(**dicc)
# **可以对词典的值进行解包，但此时键只能是字符串
demo(*dic.values())

print('\n\n\n')
print('--------------------')

def demo(a,b,c):
    print(a,b,c)
demo(1,*(2,3))

# demo(a=1,*(2,3))
# wrong
# 序列解包相当于位置参数 优先处理 而a是关键参数

# 内置函数map()可以将一个函数作用到一个序列或迭代器对象上
print(list(map(lambda x,y:x+y,[1,2,3,4],[5,6,7,8])))
print(list(map(lambda x,y:x+y,range(1,6),range(5,9))))

# 内置函数filter将一个函数作用到一个序列上，返回该序列中使得该函数返回值为True的那些元素组成的filter对象
print(list(filter(lambda x:isinstance(x,int),[1,'2',3,'4',5,'6'])))

# 标准库functools中的reduce()函数可以将一个接受2个参数的函数以迭代的方式从左到右依次作用到一个序列或迭代器对象的所有元素上
seq=list(range(10))
print(reduce(lambda x,y:x+y,seq))

# 生成器函数
# 包含yield语句的函数可以用来创建生成器对象，这样的函数也称生成器函数。
# 每次执行到yield语句会返回一个值然后暂停或挂起后面代码的执行，下次通过生成器对象的__next__()方法、内置函数next()、for循环遍历生成器对象元素或其他方式显式“索要”数据时恢复执行。
# 生成器对象具有惰性求值的特点，适合大数据处理。
def f():
    a,b=1,1
    while True:
        yield a
        a,b=b,a+b

a=f()
for i in range(10):
    print(a.__next__(),end=' ')

print('\n----------')
# 函数嵌套定义
def myMap(iterable,op,value):
    if op not in '+-*/':
        return 'Error Operator'
    def nested(item):
        return eval(repr(item)+op+repr(value))
    return map(nested,iterable)

print(list(myMap(range(5),'*',5)))








