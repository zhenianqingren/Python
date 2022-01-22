import random
from math import pi as PI
data=list(range(20))
print(data)
random.shuffle(data)
print(data)
data.sort(key=lambda x:len(str(x)),reverse=True)
print(data)

x=[[random.randint(1,10) for j in range(5)]for i in range(5)]

for i in range(5):
    print(x[i])

print('---------')
f=lambda x,y,z:x+y+z
print(f(1,2,3))

def CircleArea(r):
    if isinstance(r,(int,float)) and r>0:
        print(PI*(r**2))
    else:
        print('ILEAGAL INPUT')

CircleArea('a')
CircleArea(3)

def demo(ls,k):
    x=ls[:k]
    x.reverse()
    y=ls[k:]
    y.reverse()
    r=x+y
    r.reverse()
    return r

ls=list(range(1,21))
print(type(range(10)))
print(ls)
print(demo(ls,5))
print('----------------------\n')
test1=ls[:5]
test2=ls[6:]
print(id(ls))
print(id(test1))
print(id(test2))
test1[0]=-1
print(ls)
print(test1)

