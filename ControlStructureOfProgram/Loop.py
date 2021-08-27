import time
# for <loop variable> in <ergodic structure>:
#   block
for i in range(1,10,2):
    print(i)

for c in "Python123":
    print(c,end="")
    time.sleep(0.1)

for item in [123,"Python",456]:
    print(item,end="  ")
    time.sleep(0.3)

# for line in File:
#   block

a=3
while a>0:
    print(a)
    a=a-1

for c in "PYTHON":
    if c== 'T':
        continue
    print(c,end="")
else:
    print("Normal Execution")
# else can be used to determine whether the loop has completed normally
for c in "PYTHON":
    if c=='T':
        break
    print(c,end="")
else:
    print("Normal Execution")