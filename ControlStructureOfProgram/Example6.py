import random
import time
pi = 0
N = 100
for k in range (N):
    pi+=1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("The value of pi is {}".format(pi))

DARTS=1000*1000
hits=0.0
start=time.perf_counter()
for i in range (1,DARTS+1):
    x,y=random.random(),random.random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits+=1
end=time.perf_counter()
pi=4*(hits/DARTS)
print("The value of pi is {}".format(pi))
print(end-start)
