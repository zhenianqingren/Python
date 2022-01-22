# Python 3.x完全支持中文字符，默认使用UTF8编码格式，
# # 无论是一个数字、英文字母，还是一个汉字，在统计字符串长度时都按一个字符对待和处理。
s = '合肥工业大学HFUT'
print(len(s))
# str()：函数返回一个用户易读的表达形式。
# repr()：产生一个解释器易读的表达形式。
print(str(s))
print(repr(s))
print(str(1 / 7))
print(repr(1 / 7))
# repr() 函数可以转义字符串中的特殊字符
hello = 'hello, HFUT\n'
print(repr(hello))
# repr() 的参数可以是 Python 的任何对象
x = 3.25 * 10
y = 20 * 20
print(repr((x, y, ('Google', 'HFUT'))))
# 在Python中，字符串属于不可变序列类型，除了支持序列通用方法（包括分片操作）以外，还支持特有的字符串操作方法。
# s[0]='1' wrong
# Python字符串驻留机制：对于短字符串，将其赋值给多个不同的对象时，
# 内存中只有一个副本，多个对象共享该副本。长字符串不遵守驻留机制。
t1 = 'test'
t2 = 'test'
print(id(t1) == id(t2))
print('-------------------------------------------------------------------------')
# 字符串格式化
x = 1235
so = "%o" % x
print(so)
sh = "%x" % x
print(sh)
se = "%e" % x
print(se)
print(chr(ord("3") + 1))
print('%s' % [1, 2, 3])  # 直接把对象转换成字符串
print(str((1, 2, 3)))
print(list(str([1, 2, 3])))  # 字符串中的每个字符都成为列表的元素
n = 81
print(eval('n+5'))
print('-------------------------------------------------------------------------')
# format()
position = (5, 8, 13)
print("X:{0[0]};Y:{0[1]};Z:{0[2]}".format(position))
# : <fill> <alignment> <width>    <,>(thousands separator for numbers) <.accuracy>(the precision of a floating-point number or the maximum output length of a string) <type>(Integer:b c d o x x Float:e E f %)
print("{:=^20}".format("Python"))
print("{:+<20}".format("Python"))
print("{:->20}".format("Python"))

print("{:=^20.2f}".format(123456.789))
print("{0:b} {0:c} {0:d} {0:o} {0:x} {0:x}".format(425))
print("{0:e} {0:E} {0:f} {0:%}".format(3.14))
print('-------------------------------------------------------------------------')

weather = [("Monday", "rainy"), ("Tuesday", "sunny"),
           ("Wednesday", "sunny"), ("Thursday", "rainy"),
           ("Friday", "cloudy")]
formatter = "Weather of '{0[0]}' is '{0[1]}'".format
for item in map(formatter, weather):
    print(item)
for item in weather:  # 两种写法等效
    print(formatter(item))
# find()和rfind方法分别用来查找一个字符串在另一个字符串指定范围（默认是整个字符串）中首次和最后一次出现的位置，如果不存在则返回-1
# index()和rindex()方法用来返回一个字符串在另一个字符串指定范围中首次和最后一次出现的位置，如果不存在则抛出异常；
print('-------------------------------------------------------------------------')
# split()和rsplit()方法分别用来以指定字符为分隔符，把当前字符串从左往右或从右往左分隔成多个字符串，并返回包含分隔结果的列表；
# partition()和rpartition()用来以指定字符串为分隔符将原字符串分隔为3部分，
# 即分隔符前的字符串、分隔符字符串、分隔符后的字符串，如果指定的分隔符不在原字符串中，则返回原字符串和两个空字符串。
s = "apple,peach,banana,pear"
print(s.split(','))
print(s.partition(','))
print(s.rpartition('banana'))
# split()和rsplit()方法如果不指定分隔符，则字符串中的任何空白符号
# （包括空格、换行符、制表符等）都被认为是分隔符，返回包含最终分隔符的列表
# split()和rsplit()方法还允许指定最大分割次数。
# 分隔符的两侧必须是非空白元素
# 把连续多个 (空白字符等)看作一个分隔符。
s = '\n\nhello\t\t world \n\n\n My name is Python   '
print(s.split(None, 1))
print(s.rsplit(None, 1))
# 然而，明确传递参数指定split()使用的分隔符时，情况是不一样的。
print('\ta\t\t\tbb\t\tccc'.split('\t'))
print('\ta\t\t\tbb\t\tccc'.split())
# 字符串连接join()
s = 'good'
print(''.join([s] * 5))
# capitalize() 字符串首字符大写
# title()  每个单词首字母大写
# swapcase()  大小写互换
s = '中国 美国'
print(s.replace('中国', '中华人民共和国'))
print(s.replace('美国', '美利坚合众国'))
print('-------------------------------------------------------------------------')
# 字符串对象的maketrans()方法用来生成字符映射表字典，
# 而translate()方法用来根据映射表中定义的对应关系转换字符串并替换其中的字符，
# 使用这两个方法的组合可以同时处理多个字符。
# 创建映射表，将字符"abcdef123"一一对应地转换为"uvwxyz@#$"
table = ''.maketrans('abcdef123', 'uvwxyz@#$')
print(table)
s = "Python is a greate programming language. I like it!"
# 按映射表进行替换
print(s.translate(table))
print('-------------------------------------------------------------------------')
# strip()、rstrip()、lstrip()
# 这三个函数的参数指定的字符串并不作为一个整体对待，而是在原字符串的两侧、右侧、左侧删除参数字符串中包含的所有字符，
# 一层一层地从外往里扒。
print('aabbccddeeeffg'.strip('af'))  # f在内测，所以不删除
print('aabbccddeeeffg'.strip('gbf'))
text = '''姓名：张三
年龄：39
性别男
职业  学生
籍贯：  地球'''
infomation = text.split('\n')
for item in infomation:
    print(item[:2], item[2:].strip('： '), sep='：')
print('-------------------------------------------------------------------------')
# s.startswith(t)、s.endswith(t)，判断字符串是否以指定字符串开始或结束
# 切片也适用于字符串，但仅限于读取其中的元素，不支持字符串修改。

# str.encode(encoding=‘UTF-8’,errors=‘strict’) 以指定的编码格式编码字符串
# bytes.decode(encoding="utf-8", errors="strict")        以指定的编码格式解码 bytes 对象。默认编码为 'utf-8’
# encoding -- 要使用的编码，如: UTF-8。
# errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。
# 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'
# 以及通过 codecs.register_error() 注册的任何值。
s = 'abc123合工大'
s_utf8 = s.encode(encoding='utf-8', errors='stict')
s_gbk = s.encode(encoding='GBK', errors='strict')
print(s_utf8)
print(s_gbk)
print('-------------------------------------------------------------------------')
# Pytho标准库zlib中提供的compress()和decompress()函数可以用于字节串的压缩和解压缩。
import zlib

s_com = zlib.compress(s_gbk)
s_decom = zlib.decompress(s_com)
print(len(s_com), len(s_decom))
# Python标准库string中定义数字字符、标点符号、英文字母、大写字母、小写字母等常量。
import string

print(string.ascii_letters)
print(string.digits)
print('-------------------------------------------------------------------------')
# 随机密码生成原理
import random

print(''.join([random.choice(string.digits + string.ascii_letters) for i in range(8)]))
print('-------------------------------------------------------------------------')
# 编写程序，把一个英文句子中的单词倒置，标点符号不倒置，例如 I like python. 经过函数后变为：python like I
s = 'I like python'
print(' '.join(reversed(s.split(' '))))
print('-------------------------------------------------------------------------')
# 编写程序，查找一个字符串中最长的数字子串。
s = ''.join([random.choice(string.digits + 'aiuvbopt') for i in range(40)])
t = []
res = []
for ch in s:
    if '0' <= ch <= '9':
        t.append(ch)
    elif t:
        res.append(''.join(t))
        t = []
if t:
    res.append(''.join(t))
if res:
    print(max(res, key=len))
print('-------------------------------------------------------------------------')
# 正则表达式
import re

text = 'alpha. beta....gamma delta'  # 测试用的字符串
print(re.split('[\.]+', text))  # 指定字符分割
print(re.split('[\.]+', text, maxsplit=1))  # 最多分割1次
pat = '[a-zA-Z]+'  # 匹配所有单词
print(re.findall(pat, text))
# re.sub 语法：re.sub(pattern, repl, string, count=0, flags=0)
#    前三个必选参数：pattern, repl, string，后两个可选参数：count, flags

# pattern，表示正则中的模式字符串
# repl，表示要被替换的，可以是字符串也可以是函数
# string，要处理的字符串，即替换后的结果字符串，若过滤则设置为空 ''
# count，限定替换的个数，默认为空或0，表示替换所有
# flags，匹配模式
pat = '{name}'
text='Dear {name}...'
print(re.sub(pat,'C++',text))
print(re.sub('a',lambda x:x.group(0).upper(),'abc afhu aDOP'))
print(type(re.sub('a',lambda x:x.group(0).upper(),'abc afhu aDOP')))
s = "It's a very good good idea"
print(re.sub(r'(\b\w+) \1', r'\1',s))     #处理连续的重复单词 注意 \w+)后的空格
print('-------------------------------------------------------------------------')
example = 'Hefei University of Technology'
pattern = re.compile(r'\b\w+\b')
print(pattern.findall(example))
pattern=re.compile(r'\bH\w+\b')
print(pattern.findall(example))
pattern = re.compile(r'\w+y\b')
print(pattern.findall(example))
pattern = re.compile(r'\b[a-zA-Z]{2}\b') #查找2个字母长的单词
print(pattern.findall(example))
s = 'ab134ab98723jafjweoruiagab'
m = re.search(r'((ab).*){2}.*(ab)', s)#在s中查找ab的第3次出现
print(m.group(3))
print(m.span(3))
print(s[24:])
# []表示范围,匹配[]内的任一字符
# ()表示一个子模式,括号内看作一个整体





