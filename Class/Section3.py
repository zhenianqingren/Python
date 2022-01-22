import math
import itertools

for i in range(100,1000):
    l=list(map(lambda x:int(x)**3,str(i)))
    if(sum(l)==i):
        print(i)

n=int(input('Please input an integer'))
m=math.ceil(math.sqrt(n)+1)
for i in range(2,m):
    if n%i==0 and i<n:
        print('No')
        break
else:
    print('Yes')

n,i=eval(input('n:  ')),eval(input('i:  '))
print(int(math.factorial(n)/math.factorial(i)/math.factorial(n-i)))

print(len(tuple(itertools.combinations(range(8),3))))

newlist=list(filter(lambda x:x>5,[1,2,3,4,5,6,7,8,9,10,11,12]))
print(newlist)