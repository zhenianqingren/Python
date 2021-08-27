# Text progress bar
import time
print("Execution Start".center(25,'='))
scale=10
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
print("Execution End".center(25,'='))

for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.01)

print("Execution Start".center(25,'='))
scale=50
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)
print("\n"+"Execution End".center(25,'='))