# format
# def <NameOfFunction> (<essential parameters>,<optional parameters>):
#   <block>
# return <>

# variable parameters
def fact(n,*b):
    s=1
    for i in range(1,n+1):
        s*=i
    for item in b:
        s*=item
    return s

print(fact(5,1,2,3))
# When a function is called, parameters can be passed by location or name
def fun(n,m=1):
    for i in range(1,n+1):
        n*=i
    return n+m
print(fun(10,5))
print(fun(m=5,n=10))

# Function can return 0 or more results
def func(a,b,c):
    return a+b,a+c,b+c
# The result returned is a tuple type
# Or
a,b,c=func(1,2,3)
print(a,b,c)

# Rule 1:
# When a global variable is used inside a function, add global before the variable

# Rule 2:
# A local variable is a composite data type and is not created inside a function so it is equivalent to a global variable

# lambda ->anonymous function
# Format: <Name of Function> = lambda <parameters>: <expression>
f=lambda x,y:x+y
print(f(1,2))
f=lambda :print("Hello World")
f()









