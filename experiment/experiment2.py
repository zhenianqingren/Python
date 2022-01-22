import string
import random
import collections
import re
def RandomStr():
    # 1.
    str_set=string.ascii_letters+string.digits+string.punctuation
    temp_ls=[random.choice(str_set) for k in range(1000)]
    ss="".join(temp_ls)
    my_dict={}
    for s in ss:
        my_dict[s]=my_dict.get(s,0)+1
    print(my_dict)
    # 2.
    ans = collections.Counter(ss)
    print(type(ans))
    print(ans)
# RandomStr()

def SetFunction():
#     数字
    setA=set({})
    setB=set({})
    size_A=eval(input("size of setA:"))
    size_B=eval(input("size of setB:"))
    print("input element of setA")
    for i in range(size_A):
        elem=eval(input('NO.{}'.format(i+1)))
        setA.add(elem)
    print('input element of setB')
    for i in range(size_B):
        elem=eval(input('NO.{}'.format(i+1)))
        setB.add(elem)
    print('intersection:')
    print(setA&setB)
    print('union:')
    print(setA|setB)
    print('setA-setB:')
    print(setA-setB)
    print('setB-setA:')
    print(setB-setA)

# SetFunction()

class Set():
    def __init__(self):
        self.setA=[]
        self.setB=[]
        size_A = eval(input("size of setA:"))
        size_B = eval(input("size of setB:"))
        print("input element of setA")
        for i in range(size_A):
            elem = eval(input('NO.{}'.format(i + 1)))
            if elem not in self.setA:
                self.setA.append(elem)
        print('input element of setB')
        for i in range(size_B):
            elem = eval(input('NO.{}'.format(i + 1)))
            if elem not in self.setB:
                self.setB.append(elem)
    def SetAandSetB(self):
        temp=set({})
        for elem in self.setA:
            if elem in self.setB:
                temp.add(elem)
        return temp
    def SetAorSetB(self):
        temp=set({})

        for elem in self.setA:
            temp.add(elem)
        for elem in self.setB:
            if elem not in temp:
                temp.add(elem)
        return temp
    def SetA_SetB(self):
        temp=set({})
        for elem in self.setA:
            if elem not in self.setB:
                temp.add(elem)
        return temp
    def SetB_SetA(self):
        temp=set({})
        for elem in self.setB:
            if elem not in self.setA:
                temp.add(elem)
        return temp
    def PrintResult(self):
        print('setA:')
        print(self.setA)
        print('setB:')
        print(self.setB)
        print('intersection:')
        print(self.SetAandSetB())
        print('union:')
        print(self.SetAorSetB())
        print('setA-setB:')
        print(self.SetA_SetB())
        print('setB-setA:')
        print(self.SetB_SetA())

# MySet=Set()
# MySet.PrintResult()

def NestedList(m,n):
    # return [[elem for ]for i in range(n)]
    size_num=n//2
    size_str=n-size_num
    ls1=[["".join(random.sample(string.digits+string.punctuation+string.ascii_letters,random.randint(1,m)))] for i in range(size_str)]
    ls2=[[int("".join(random.sample(string.digits,random.randint(1,m))))]for i in range(size_num)]
    ls=ls1+ls2
    ls.sort(key=lambda x:len(str(x[0])))
    print(ls)

# NestedList(8,50)

def ListSlice():
    origin=[random.randint(1,100)for i in range(15)]
    newList=origin[:]
    reverseList=origin[::-1]
    evenList=origin[::2]
    print(newList)
    print(reverseList)
    print(evenList)

# ListSlice()

def GenerateTuple(n,m):
    case=tuple(filter(lambda x:x%2==1,(random.randint(0,m)for i in range(n))))
    print(case)

# GenerateTuple(50,50)

def GenerateDict():
    Str=input('Please input a sentence in English')
    strlist=Str.split(' ')
    mydict=dict({})
    for elem in strlist:
        mydict[elem]=mydict.get(elem,0)+1
    mydict=mydict.items()
    for item in mydict:
        print(list(item)[0]+':',list(item)[1])

# GenerateDict()

def MatchStr():
    Str=input('Please input a sentence in English')
    strList=Str.split(' ')
    strList=list(filter(lambda x:len(x)==3,strList))
    print(strList)

# MatchStr()