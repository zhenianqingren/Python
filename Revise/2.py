aList = [3, 4, 5]
print(id(aList))
aList = aList + [7] * 10000
print(id(aList))
bList = aList.copy()
print(id(bList))
print('------------------------------------------------')
# Python采用的是基于值的自动内存管理方式，当为对象修改值时，并不是真的直接修改变量的值，而是使变量指向新的值，
# 这对于Python所有类型的变量都是一样的。
a = [1, 2, 3]
print(id(a))
a = [1, 2]
print(id(a))
print('------------------------------------------------')
# 列表中包含的是元素值的引用，而不是直接包含元素值。
# 如果是直接修改序列变量的值，则与Python普通变量的情况是一样的
# 如果是通过下标来修改序列中元素的值或通过可变序列对象自身提供的方法来增加和删除元素时，
# 序列对象在内存中的起始地址是不变的，仅仅是被改变值的元素地址发生变化，也就是所谓的“原地操作”。
a = [1, 2, 4]
b = [1, 2, 3]
print(a == b)
print(id(a) == id(b))
print(id(a[0]) == id(b[0]))
a = [1, 2, 3]
print(a == b)
print(id(a) == id(b))
print(id(a))
print(id(b))
a[1] = 500
print(id(a))
print(b)
print('------------------------------------------------')
# 当使用*运算符将包含列表的列表重复并创建新列表时，并不是复制子列表值，而是复制已有元素的引用。
# 因此，当修改其中一个值时，相应的引用也会被修改。
a = [1, 2, 3, 4]
print(id(a))
a = a * 4
print(id(a))
a[2] = 50
print(a)

x = [[None],[None]] * 3
print(x)
x[0][0] = 5
print(x)
print('------------------------------------------------')
# 使用列表对象的remove()方法删除首次出现的指定元素，如
# 果列表中不存在要删除的元素，则抛出异常。
x = [1, 2, 1, 2, 1, 1, 1]
for item in x:
    if item == 1:
        x.remove(item)
print(x)
# 上面这段代码的逻辑是错误的。
# 在删除列表元素时，Python会自动对列表内存进行收缩并移动列表元素以保证所有元素之间没有空隙，
# 增加列表元素时也会自动扩展内存并对元素进行移动以保证元素之间没有空隙。
# 每当插入或删除一个元素之后，该元素位置后面所有元素的索引就都改变了。
# 正确的代码
x = [1, 2, 1, 2, 1, 1, 1]
for i in range(len(x) - 1, -1, -1):  # 从后往前删
    if x[i] == 1:
        del x[i]
print(x)
print('------------------------------------------------')
aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
print(aList[::])  # 返回包含所有元素的新列表
print(aList[::-1])  # 逆序的所有元素
print(aList[::2])  # 偶数位置，隔一个取一个
print(aList[1::2])  # 奇数位置，隔一个取一个
print(aList[3::])  # 从下标3开始的所有元素
print(aList[3:6])  # 下标在[3, 6)之间的所有元素
print(aList[0:100:1])  # 前100个元素，自动截断
print(aList[100:])  # 下标100之后的所有元素，自动截断
# print(aList[100])                           #直接使用下标访问会发生越界
aList[::2] = [0] * 5  # 替换偶数位置上的元素
print(aList)
for e in aList:
    e = -1
print(aList)  # 不会改变,e是深拷贝
t = [1, 2, 3, 4]
T = t[:]
print(id(T) == id(t))
T[0] = 1000
print(t)  # 基本数据类型不会变
t = [[1], [2], [3]]
T = t[:]
T[0][0] = -1
print(t)
print('------------------------------------------------')
# 切片返回的是列表元素的浅复制
# 如果原列表中包含列表之类的可变数据类型，由于浅复制时只是把子列表的引用复制到新列表中，因而修改任何一个都会影响另外一个。
# 标准库copy中的deepcopy()函数实现深复制。
# 所谓深复制，是指对原列表中的元素进行递归，把所有的值都复制到新列表中，对嵌套的子列表不再是复制引用。
# 新列表和原列表是互相独立，修改任何一个都不会影响另外一个
test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(reversed(test)))  # 一次性使用，返回可迭代对象
print(test)
print(sum(test))
print(sum(test, 100))
print('------------------------------------------------')
# zip()函数返回可迭代的zip对象
aList = [1, 2, 3]
bList = [4, 5, 6]
cList = zip(aList, bList)
print(list(cList))  # 每个元素是一个元组
print('------------------------------------------------')
# enumerate(列表):枚举列表元素，返回枚举对象
# 其中每个元素为包含下标和值的元组。
# 该函数对元组、字符串同样有效。
for item in enumerate('abcdef'):
    print(item)
print(type(list(enumerate('abcdefg'))[0]))
print('------------------------------------------------')
# 列表推导式
L = [x * y for x in range(1, 5) for y in range(1, 4)]
print(L)
aList = [x * x for x in range(10)]
print(aList)
print('------------------------------------------------')
# 编写算法实现嵌套列表的平铺
# [[1,2,3], [4,5,6]]  [1, 2, 3, 4, 5, 6]
ori = [[1, 2, 3], [4, 5, 6]]
gen = [e for l in ori for e in l]
print(gen)
print('------------------------------------------------')
# 使用列表推导式实现矩阵转置
mar = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Tmar = [[row[i] for row in mar] for i in range(4)]
print(Tmar)
# 使用列表推导式生成100以内的所有素数
import math

print([p for p in range(2, 100) if 0 not in [p % d for d in range(2, int(p ** 0.5 + 1))]])
print(list(range(2, int(3 ** 0.5 + 1))))
print('------------------------------------------------')
# 元组和列表类似，但属于不可变序列，元组一旦创建，用任何方法都不可以修改其元素。
# 元组的定义方式和列表相同，但定义时所有元素是放在一对圆括号“（）”中，而不是方括号中。
aTuple = ('a', 'b', 'mpilgrim', 'z', 'example')
a = (3,)  # 包含一个元素的元组，最后必须多写个逗号
a = 3,
print(type(a))
print('------------------------------------------------')
# 元组一旦定义就不允许更改。
# 元组没有append()、extend()和insert()等方法，无法向元组中添加元素。
# 元组没有remove()或pop()方法，也无法对元组元素进行del操作，不能从元组中删除元素。
# 序列解包
# 当函数或方法返回元组时，将元组中值赋给变量序列中的变量，这个过程就叫做序列解包。
# 可以使用序列解包功能对多个变量同时赋值
x, y, z = 1, 2, 3  # 多个变量同时赋值
print(x, y, z)
v_tuple = (False, 3.5, 'exp')
(x, y, z) = v_tuple
print(x, y, z)
x, y, z = v_tuple
print(x, y, z)
x, y, z = range(3)  # 可以对range对象进行序列解包
print(x, y, z)
x, y, z = iter([1, 2, 3])  # 使用迭代器对象进行序列解包
print(x, y, z)
x, y, z = map(str, range(3))  # 使用可迭代的map对象进行序列解包
print(x, y, z)
a, b = 1, 2
a, b = b, a  # 交换两个变量的值
print(a, b)
x, y, z = sorted([1, 3, 2])  # sorted()函数返回排序后的列表
print(x, y, z)
a, b, c = 'ABC'  # 字符串也支持序列解包
print(a, b, c)
x = [1, 2, 3, 4, 5, 6]
x[:3] = map(str, range(5))  # 切片也支持序列解包
print(x)
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
for k, v in zip(keys, values):
    print((k, v), end=' ')
print()
aList = [1, 2, 3]
bList = [4, 5, 6]
cList = [7, 8, 9]
dList = zip(aList, bList, cList)
for index, value in enumerate(dList):
    print(index, ':', value)
l=[1,2,3]
x,y,z=l
print(x,y,z)
print('------------------------------------------------')
# 生成器推导式的结果是一个生成器对象。
# 使用生成器对象的元素时，可以根据需要将其转化为列表或元组，也可以使用生成器对象__next__()方法或内置函数next()进行遍历，
# 或者直接将其作为迭代器对象来使用。
# 生成器对象具有惰性求值的特点，只在需要时生成新元素，比列表推导式具有更高的效率，空间占用非常少，尤其适合大数据处理的场合。
# 不管用哪种方法访问生成器对象，都无法再次访问已访问过的元素。
g = ((i + 2) ** 2 for i in range(10))  # 创建生成器对象
print(g)
print(tuple(g))
# g = ((i+2)**2 for i in range(10))
print(list(g))  # 不管用哪种方法访问生成器对象，都无法再次访问已访问过的元素。
# 使用for循环直接迭代生成器对象中的元素
g = ((i + 2) ** 2 for i in range(10))
for item in g:
    print(item, end=' ')
print('------------------------------------------------')
# 字典是无序、可变序列。
# 定义字典时，每个元素的键和值用冒号分隔，元素之间用逗号分隔，所有的元素放在一对大括号“｛｝”中。
# 字典中的键可以为任意不可变数据，比如整数、实数、复数、字符串、元组等等。
# globals()返回包含当前作用域内所有全局变量和值的字典
# locals()返回包含当前作用域内所有局部变量和值的字典
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
dictionary = dict(zip(keys, values))
print(dictionary)
d = dict(name='Dog', age=37)
print(d)
adict = dict.fromkeys(['name', 'age', 'sex'])
print(adict)
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(a == b == c == d == e == f)
aDict = {'name': 'Dong', 'sex': 'male', 'age': 37}
print(aDict.get('address'))
print(aDict.get('address', 'SDIBT'))
aDict['address'] = 'Not Addressed'
aDict['score'] = aDict.get('score', [])  # 字典元素的添加
aDict['score'].append(98)
aDict['score'].append(97)
print(aDict)
for key in aDict:  # 不加特殊说明，默认输出键
    print(key)
print(aDict.keys())  # 返回所有键
# 使用del删除字典中指定键的元素
# 使用字典对象的clear()方法来删除字典中所有元素
# 使用字典对象的pop()方法删除并返回指定键的元素
# 使用字典对象的popitem()方法删除并返回字典中最后一个元素（返回并删除字典中的最后一对键和值）
print('------------------------------------------------')
import string
import random

x = string.digits + string.ascii_letters  # x='0123456789'
y = [random.choice(x) for i in range(1000)]
z = ''.join(y)
d = dict()
for ch in z:
    d[ch] = d.get(ch, 0) + 1
print(d)
print('------------------------------------------------')
# 字典推导式
mca = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d = {v: k for k, v in mca.items()}
print(d)
print('------------------------------------------------')
# 集合是无序、可变序列，使用一对大括号界定，元素不可重复，同一个集合中每个元素都是唯一的。
# 集合中只能包含数字、字符串、元组等不可变类型（或者说可哈希）的数据，而不能包含列表、字典、集合等可变类型的数据。
a = {3, 5}
a.add(7)  # 向集合中添加元素
print(a)
a_set = set(range(8, 14))
print(a_set)
b_set = set([0, 1, 2, 3, 0, 1, 2, 3, 7, 8])  # 自动去除重复
print(b_set)
c_set = set()  # 空集合
print(c_set)
e = {}
print(type(e))
f = {4, }
print(type(f))
print('------------------------------------------------')
# 生成不重复随机数
number = 100
data = set()
while True:
    data.add(random.randint(0, 10000))
    if len(data) == number:
        break
print(data)
print('------------------------------------------------')
# 集合推导式(set comprehensions)
s = {x.strip() for x in ('  he  ', 'she    ', '    I')}
print(s)
# 列表对象提供了sort()方法支持原地排序，而内置函数sorted()返回新列表，并不对原列表进行任何修改。
# sorted()方法可以对列表、元组、字典、range对象等进行排序。
# 列表的sort()方法和内置函数sorted()都支持key参数实现复杂排序要求。
persons = [{'name': 'Li', 'age': 40}, {'name': 'Li', 'age': 37},
           {'name': 'Dong', 'age': 43}]
print(persons)
# 使用key来指定排序依据，先按姓名升序排序，姓名相同的按年龄降序排序
print(sorted(persons, key=lambda x: (x['name'], -x['age'])))
print('------------------------------------------------')
# 有一个整数列表，要求调整元素顺序，把所有奇数都放到前面，偶数都放到后面
x = [random.randint(0, 100) for i in range(10)]
print(x)
print(sorted(x, key=lambda num: num % 2 == 0))
print(sorted(x, key=lambda num: num % 2 == 0, reverse=True))
