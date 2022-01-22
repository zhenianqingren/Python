# 构建跳转表实现多分支选择结构
# funcDict = {'1': lambda: print('You input 1'),
#             '2': lambda: print('You input 2'),
#             '3': lambda: print('You input 3')}
# x = input('Input an integer to call different function:')
# func = funcDict.get(x, None)
# if func:
#     func()
# else:
#     print('Wrong integer.')
# 用户输入若干个分数，求所有分数的平均分。每输入一个分数后
# 询问是否继续输入下一个分数，回答“yes”就继续输入下一个
# 分数，回答“no”就停止输入分数。
print('---------------------------------------------------------------')
# numbers = []
# while True:
#     x = input('请输入一个成绩: ')
#     try:
#         numbers.append(float(x))
#     except:
#         print('不是合法成绩')
#     while True:
#         flag = input('继续输入吗(yes/no): ').lower()
#         if flag not in ('yes', 'no'):
#             print('Wrong')
#         else:
#             break
#     if flag == 'no':
#         break
# if (len(numbers) != 0):
#     print(sum(numbers) / len(numbers))
# 编写程序，判断今天是今年的第几天？
import time

date = time.localtime()
year, month, day = date[:3]
day_month = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    day_month[1] = 29
if (month == 1):
    print(day)
else:
    print(sum(day_month[:month - 1]) + day)
print('---------------------------------------------------------------')
# 在循环中应尽量引用局部变量，因为局部变量的查询和访问速度比全局变量略块。
# 在使用模块中的方法时，可以通过将其直接导入来减少查询次数和提高运行速度。
for n in range(100, 1, -1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:  # 此处的else与break相对，意思是若是自然执行完毕而不是被跳出时则执行以下两个操作
        print(n)
        break
for s in "Hello Python":
    if s == "o":
        continue
        #若是break 则不会执行else中的语句
    print(s, end="")
else:
    print("exit")
print('---------------------------------------------------------------')
# 水仙花数
for n in range(100,1000):
    i,j,k=map(int,str(n))
    if i**3+j**3+k**3==n:
        print(n)
print('---------------------------------------------------------------')
# 判断一个数字是否为丑数。
# 一个数的因数如果只包含2、3、5，那么这个数是丑数
for n in range(100,1000):
    num=n
    for i in (2,3,5):
        while True:
            m,r=divmod(n,i)
            if r!=0:
                break
            else:
                n=m
    if n==1:
        print(num)
print('---------------------------------------------------------------')
try:
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx = eval(input("请输入一个整数: "))
    print(alp[idx])
except:
    print("输入错误，请输入一个整数!")
else:
    print("没有发生异常")
finally:
    print('End of program')

def function5():
    def DayUp(dayfactor):
        result=1.0
        for i in range(1,366):
            if i%7 in [0,6]:
                result=result*(1-0.01)
            else:
                result=result*(1+dayfactor)
        return result
    factor=0.01
    while round(DayUp(factor),2) < 37.78:
        factor=factor+0.001
    print('每天要努力{}'.format(round(factor,3)))