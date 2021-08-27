import time
# time.time() Get the current timestamp, that is, the time value inside the computer, floating-point number
print(time.time())
# time.ctime() Get the current time which can be recognized easily
print(time.ctime())
# time.gmtime() Get the current time the format of which can be handled by computer
print(time.gmtime())

# time formatting    Presentation template needed
# The presentation template consists of specific formatting controls ,like string
# %Y :2021 %m :11 %B :April %b :april %d :31 %A :Monday %a :Mon %H(24h) %I(12h) %p :AM,PM %M(minute) %S(seconds)

# strftime And strptime
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))
print(time.strptime("2021-08-07 03:25:45","%Y-%m-%d %H:%M:%S"))
# time.perf_counter() Returns an accurate time count value at the CPU level, in seconds
start=time.perf_counter()
for i in range(100):
    print(" ",end="")
end=time.perf_counter()
print("\n",end-start)
#time.sleep(sec) make the program sleep for a specified period of time
start=time.perf_counter()
time.sleep(3)
end=time.perf_counter()
print(end-start)



