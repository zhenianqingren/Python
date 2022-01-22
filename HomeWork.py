import random
import math
def GuessNumber1(lo,hi):#数字范围
    answer=random.randint(lo,hi)
    num=eval(input('请输入你的猜测：'))
    if num>answer:
        print('too large,the correct answer is {}'.format(answer))
    elif num<answer:
        print('too small,the correct answer is {}'.format(answer))
    else:
        print('right')

# GuessNumber1(1,20)

def GuessNumber2(lo,hi,chance):
    answer = random.randint(lo,hi)
    isright=False
    while chance>0:
        num = eval(input('请输入你的猜测：'))
        if num > answer:
            print('too large')
        elif num < answer:
            print('too small')
        else:
            print('right')
            isright=True
            break
        chance=chance-1
    if not isright:
        print('chances have been empty,the correct answer is {}'.format(answer))
# GuessNumber2(1,100,3)

def fibonacci(n):
    ls=[]
    a=0
    b=1
    while a<n:
        ls.append(a)
        a,b=b,a+b
    print(ls)

# fibonacci(10)

def OutputList():
    legal=False
    while not legal:
        n=eval(input('请输入一个大于2的自然数'))
        if n>2:
            legal=True

    def isPrimeNum(N):
        isPrime=True
        for i in range(2,int(math.sqrt(N))+1+1):
            if N%i==0 and N!=2:
                isPrime=False
                break
        return isPrime

    ls=[i for i in range(2,n) if isPrimeNum(i)]

    print(ls)

# OutputList()

def PalindromeNum(s):
    i,j=0,len(s)-1
    isPalindrome=True
    while(i<=j):
        if s[i]!=s[j]:
            isPalindrome=False
            break
        else:
            i=i+1
            j=j-1
    if isPalindrome:
        print('Yes')
    else:
        print('No')

# PalindromeNum('aabbccbbaa')


def function4(n,lo,hi):
    ls=[random.randint(lo,hi) for i in range(n)]
    average=sum(ls)/n
    print(ls)
    for i in range(n-1,-1,-1):
        if ls[i]<=average:
            del ls[i]
    ls.insert(0,average)
    print(ls)
    return tuple(ls)

# function5(5,1,10)

def function5():
    def DayUp(dayfactor):
        result=1.0
        for i in range(1,366):
            if i%7 in [0,6]:
                result=result*(1-0.01)
            else:
                result=result*(1+dayfactor)
        print(result)
        return result
    factor=0.01
    while DayUp(factor) < 37.78:
        factor=factor+0.001
    print('每天要努力{}'.format(factor))

function5()







