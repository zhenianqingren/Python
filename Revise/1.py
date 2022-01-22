x = 'Hello world.'
print(type(x))
print(isinstance(3, int))   #isinstance():测试对象是否是某个类型的实例
print('--------------------------------------')
# 字符串和元组属于不可变序列，不能通过下标的方式来修改其中的元素值，试图修改元组中元素的值时会抛出异常。
# Python采用的是基于值的内存管理方式，如果为不同变量赋值为相同值，这个值在内存中只有一份，多个变量指向同一块内存地址。
x = 3
print(id(x))
y = 3
print(id(y))
x = [1, 1, 1, 1]
print(id(x[0]) == id(x[1]))
x=[2,2,3]
y=[2,2,3]
print(id(x)==id(x[0]))
print(id(x)==id(y))
print(id(x[0])==id(y[0]))
print('--------------------------------------')
a = 3+4j
print(a.real)
print(a.imag)
print('--------------------------------------')
# 字符串界定符前面加字母r或R表示原始字符串，其中的特殊字符不 进行转义，但字符串的最后一个字符不能是\。
#range()是用来生成指定范围数字的内置函数 一个可迭代序列 range([start,] end [, step] ) 其中包含左闭右开区间[start,end)内以step为步长的整数
# 不支持++运算符
print(1,2,3,sep='*')
print('--------------------------------------')

from math import sin
print(sin(3))
from math import sin as f
print(f(3))
print('--------------------------------------')

# .py：Python源文件，由Python解释器负责解释执行。
# .pyw：Python源文件，常用于图形界面程序文件。
# .pyc：Python字节码文件，无法使用文本编辑器直接查看其内容，可用
#  于隐藏Python源代码和提高运行速度。
# .pyd：一般是由其他语言编写并编译的二进制文件，常用于实现某些软
#  件工具的Python编程接口插件或Python动态链接库。
print(__name__)
print('--------------------------------------')
# 已知三角形的两边长及其夹角，求第三边长。
import math
x = input('输入两边长及夹角（度）：')
a, b, theta = map(float, x.split())
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(theta*math.pi/180))
print('c=', c)
print('--------------------------------------')
# 任意输入三个英文单词，按字典顺序输出。
s = input('x, y, z=')
x, y, z = sorted(s.split(','))#sorted 默认升序
print(x, y, z)


