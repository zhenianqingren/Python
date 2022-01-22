import re
reg1=r'\d+'
reg2=r'\d'
reg3=r'a\d+'
reg4=r'.\d+'
text='aaa123456bbbccc789'
print(re.search(reg1,text))
print(re.search(reg2,text))
print(re.search(reg3,text))
print(re.search(reg4,text))

reg=r'car\b'
print(re.search(reg,'This car is good'))
reg=r'x[0-9A-Za-z]+y'
print(re.search(reg,'x123yx1yxabyxay'))