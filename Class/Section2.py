import random

def square(x):
    return x*x

l=list(map(square,[1,2,3,4,5]))
print(l)
l=list(map(lambda x:x**2,[1,2,3,4,5,6]))
print(l)



list=[random.randint(0,10000) for i in range(20)]
print(list)

print(sum(range(1,101)))