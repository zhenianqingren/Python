# import timeit
# import string
# import random
# import re
# print(str(1/7))
# print(repr(1/7))
#
# print('Python\nPython')
# print(repr('Python\nPython'))
#
# x=3.25*10
# y=200*200
# print(repr((x,y,('Google','Microsoft'))))# repr() 的参数可以是 Python 的任何对象
#
# testString='good'
# b='good'
# p='abcde'*1000000
# q='abcde'*1000000
# print(id(testString))
# print(id(b))
# print(id(p))
# print(id(q))
# # 字符串是不可变序列
# # testString[0] wrong
# # Python字符串驻留机制：对于短字符串，将其赋值给多个不同的对象时，内存中只有一个副本，多个对象共享该副本。长字符串不遵守驻留机制。
# print('--------------\n\n\n')
# x=1235
# so='%o'%x
# print(so)
# sh='%x'%x
# print(sh)
# print('--------------\n\n')
# ss='%s'%[1,2,3,'4567']
# print(ss)
# print(type(ss))
#
# l=list(str([1,2,3]))
# for i in range(len(l)):
#     print(l[i])
#
# print('-------------\n\n')
#
# weather = [("Monday","rainy"),("Tuesday","sunny"),
#            ("Wednesday", "sunny"),("Thursday","rainy"),
#            ("Friday","cloudy")]
# formatter = "Weather of '{0[0]}' is '{0[1]}'".format
#
# for item in map(formatter,weather):
#     print(item)
#
# for item in weather:
#     print(formatter(item))
#
# print('--------------\n\n')
#
# s="apple,peach,banana,peach,pear"
# print(s.find('peach'))
# print(s.find('peach',7))
# print(s.find('peach',7,20))
# print(s.index('p'))
# print(s.index('pe'))
# # print(s.index('xxx'))
# # find()和rfind方法分别用来查找一个字符串在另一个字符串指定范围（默认是整个字符串）中首次和最后一次出现的位置，如果不存在则返回-1
# # index()和rindex()方法用来返回一个字符串在另一个字符串指定范围中首次和最后一次出现的位置，如果不存在则抛出异常
#
# # partition()和rpartition()用来以指定字符串为分隔符将原字符串分隔为3部分，
# # 即分隔符前的字符串、分隔符字符串、分隔符后的字符串，如果指定的分隔符不在原字符串中，则返回原字符串和两个空字符串
# s='apple,peach,banana,pear'
# print(s.partition(','))
# print(s.rpartition(','))
# print(s.split(','))
# print(s.rsplit(','))
# # split()和rsplit()方法还允许指定最大分割次数
# print(s.split(',',1))
# # 对于split()和rsplit()方法，
# # 如果不指定分隔符，则字符串中的任何空白符号（空格、换行符、制表符等）都将被认为是分隔符，把连续多个 (空白字符等)看作一个分隔符
# s='\n\nhello\t\tworld\n\n\nMy Name\tis Python'
# print(s.split())
# s='abcdefg'
# s=s[::-1]
# print(s)
# # 将字符串重复指定次数，并使用指定的分隔符进行连接，结果字符串最后不带分隔符
# def concat(s,n,separator):
#     return separator.join([s]*n)
# # Attention: s外的[]
# print(concat('Google',5,'-'))
#
# print(timeit.timeit("-".join(str(i**2) for i in range(100)),number=100))
# print(timeit.timeit("-".join(str(i**2) for i in range(100)),number=1000))
#
# print('\n-------------')
#
# table=''.maketrans('abcdef123','uvwxyz@#$')
# print(table)
# s='aaa ppp qqq ccc eee 333 999'
# print(s.translate(table))
# # isalnum()、isalpha()、isdigit()、isdecimal()、isnumeric()、isspace()、isupper()、islower()，
# # 用来测试字符串是否为数字或字母、是否为字母、是否为数字字符、是否为空白字符、是否为大写字母以及是否为小写字母
#
# print(string.digits)
# print(type(string.digits))
# print(string.punctuation)
# print(type(string.punctuation))
#
# # 随机密码生成原理
# base=string.digits+string.punctuation
# for i in range(5):
#     print(''.join(random.choice(base) for i in range(10)))
# print('---------------')
#
# print('----------\n')
#
# text='alpha. beta....gamma ... delta'
# print(re.split('[\.]+',text))
# pat='[a-zA-Z]+'
# print(re.findall(pat,text))
#
# pat = '{name}'
# text = 'Dear {name}...'
# print(re.sub(pat,'Mr.Python',text))#字符串替换
#
# s = 'a s d'
# print(re.sub('a|s|d', 'good', s))
#
# s = "It's a very good good idea"
# print(re.sub(r'(\b\w+) \1', r'\1', s))   #处理连续的重复单词 注意 \w+)后的空格
#
# print(re.sub('a', lambda x:x.group(0).upper(),'aaa abc abde'))#repl为可调用对象


import re                            #导入re模块
# text = 'alpha. beta....gamma delta'  #测试用的字符串
# print(re.split('[\.]+', text))       #使用指定字符作为分隔符进行分隔
#
# print(re.split('[\. ]+', text, maxsplit=2)) #最多分隔2次
#
# print(re.split('[\. ]+', text, maxsplit=1)) #最多分隔1次
#
# pat = '[a-zA-Z]+'
# print(re.findall(pat, text))                #查找所有单词
pat = '{name}'
text = 'Dear {name}...'
print(re.sub(pat, 'Mr.Python', text)) #字符串替换

s = 'a s d'
print(re.sub('a|s|d', 'good', s)) #字符串替换

s = "It's a very good good idea"
print(re.sub(r'(\b\w+) \1', r'\1', s))     #处理连续的重复单词 注意 \w+)后的空格

print(re.sub(r'((\w+) )\1', r'\2', s))

print(re.sub('a', lambda x:x.group(0).upper(),
           'aaa abc abde'))              #repl为可调用对象





































