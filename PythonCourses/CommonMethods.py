print(type({3}) in (list,tuple,dict))
print(isinstance(3,int))
print(isinstance(3j,(int,float,complex)))

x=zip("abcd","1234")
print(x)
print(list(x))

a=[1,2,3]
b=[4,5,6,7,8,9]
c=[9,9,9,9]
zipped=zip(a,b,c)
print(list(zipped))
x1,x2,x3=zip(*zip(a,b,c))
print(list(x1))
print(list(x2))
print(list(x3))
