import random
import string
import re
class Student:
    def __init__(self,ID,name,gentle,age,score):
        self.ID=ID
        self.name=name
        self.gentle=gentle
        self.age=age
        self.score=score
        self.Average()
    def SetScore(self,subject,mark):
        self.score[subject]=mark
        self.Average()
    def Average(self):
        ls=[int(item[1]) for item in self.score.items()]
        self.average=sum(ls)/len(ls)
    def PrintInfo(self):
        print('ID:'+self.ID+' name:'+self.name+' gentle:'+self.gentle+' age:'+self.age,end=' ')
        print('Chinese:{} Math:{} English:{} Average:{}'.format(self.score['Chinese'],self.score['Math'],self.score['English'],self.average))
def test1():
    file=open('info.txt',encoding='utf-8')
    StuList=[]
    for line in file.readlines():
        info=line.split()
        score=dict({})
        ID,name,gentle,age=info[0],info[1],info[2],info[3]
        for case in info[4:]:
            subject,mark=case.split(':')[0],case.split(':')[1]
            score[subject]=mark
        StuList.append(Student(ID,name,gentle,age,score))
    file.close()
    StuList[3].SetScore('Chinese','100')
    StuList[3].SetScore('Math','100')
    StuList[3].SetScore('English','100')
    StuList.sort(key=lambda stu:stu.average,reverse=True)
    i=1
    for stu in StuList:
        print('{}:  '.format(i),end='')
        stu.PrintInfo()
        i=i+1

# test1()

class Employee:
    def __init__(self,name,ID):
        self.name=name
        self.ID=ID
    def pay(self,workdays=20,daily_salary=500,subsidize=2000):
        self.salary=workdays*daily_salary+subsidize
    def show(self):
        print('name:{} ID:{} salary:{} position:Employee'.format(self.name,self.ID,self.salary))

class manager(Employee):
    def __init__(self,name,ID):
        super().__init__(name,ID)
    def pay(self,workdays=25,daily_salary=400):
        self.salary=workdays*daily_salary
    def show(self):
        print('name:{} ID:{} salary:{} position:manager'.format(self.name, self.ID, self.salary))

class salesman(Employee):
    def __init__(self,name,ID):
        super().__init__(name,ID)
    def pay(self,workdays=20,daily_salary=550,subsidize=2500):
        self.salary=workdays*daily_salary+subsidize
    def show(self):
        print('name:{} ID:{} salary:{} position:salesman'.format(self.name, self.ID, self.salary))

def main():
    man1=salesman('朱文旭',2020)
    man2=manager('朱雯序',2021)
    man1.pay()
    man2.pay()
    man1.show()
    man2.show()

# main()

class Vehicle:
    def __init__(self,MaxSpeed,weight):
        self.__MaxSpeed=MaxSpeed
        self.__weight=weight
    def UpdateMaxSpeed(self,speed):
        self.__MaxSpeed=speed
    def getMaxSpeed(self):
        return self.__MaxSpeed

class Bicycle(Vehicle):
    def __init__(self,height):
        self.__height=height
    def SetMaxSpeed(self,MaxSpeed):
        self.UpdateMaxSpeed(MaxSpeed)
    def __get(self):
        return self.__height
    def __set(self,height):
        self.__height=height
    def __del(self):
        del self.__height
    height=property(__get,__set,__del)
    def show(self):
        print('Type:Bicycle  height:{}m  MaxSpeed:{}m/s'.format(self.__height,self.getMaxSpeed()))

# mybike=Bicycle(1.5)
# mybike.SetMaxSpeed(15)
# mybike.show()
# mybike.height=999
# mybike.show()
# del mybike.height
# mybike.show()

class Myqueue:
    def __init__(self):
        self.size=random.randint(0,100)
        self.current=0
        self.data=[]
    def init(self):
        self.size=10
        self.current=0
        self.data.clear()
    def isEmpty(self):
        return self.current==0
    def isFull(self):
        return self.current==self.size
    def get(self):
        if self.isEmpty():
            print('Error:Queue is Empty')
        else:
            return self.data[0]
    def push(self,elem):
        if self.isFull():
            self.size*=2
        self.current+=1
        self.data.append(elem)
    def pop(self):
        if self.isEmpty():
            print('Error:Queue is Empty')
        else:
            self.current-=1
            del(self.data[0])

def test():
    Queue=Myqueue()
    Queue.init()
    print('size:{}'.format(Queue.size))
    print(Queue.data)
    Queue.get()
    Queue.pop()
    for i in range(10):
        Queue.push(i)
    print(Queue.isFull())
    print(Queue.get())
    Queue.pop()
    print(Queue.get())
    Queue.push(10)
    Queue.push(11)
    print('size:{}'.format(Queue.size))
    print(Queue.data)

# test()

def WriteStr(n):
    with open('string.txt','a+',encoding='utf-8') as file:
        for i in range(n):
            str="".join(random.sample(string.digits+string.punctuation+string.ascii_letters,random.randint(1,50)))
            file.write(str+'\n')
        file.seek(0)
        print(len(file.readlines()))

# WriteStr(15)

def CheckLegal(input):
    passwordList=input.split(',')
    a_z=re.compile(r'[a-z]')
    A_Z=re.compile(r'[A-Z]')
    num=re.compile(r'[0-9]')
    char=re.compile(r'[$#@]')
    final=[]
    for password in passwordList:
        if (a_z.search(password)!=None)and(A_Z.search(password)!=None)and(num.search(password)!=None)and(char.search(password)!=None)and(len(password)>=6)and(len(password)<=12):
            final.append(password)
    print(','.join(final))

# file=open('password.txt','r',encoding='utf-8')
# CheckLegal(file.read())
# file.close()







