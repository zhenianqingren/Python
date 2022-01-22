import string
import re
#
#
d={"China":"Bejing","US":"Washington","France":"Paris"}
print(d["China"])

# del d[k] delete elements in d whose key is k
# k in d :True/False
# d.keys() return all key's information in dictionary d
# d.values() return all value's information in dictionary d (list)
# d.items() return all key value pair information in dictionary d
# d.get(k,<default>) If the key k exists, the corresponding value is returned; otherwise, default is returned
# d.pop(k.<default>) If the key k exists, take out the corresponding value; otherwise, return to default
# d.popitem() randomly take a key value pair from dictionary D and return it in tuple form
# d.clear()
# len(d)
print(d.get("China","India"))
print(d.get("Russia","India"))
print(d.popitem())
d["Bratain"]="London"
print(d["Bratain"])
test=list(d.items())
for item in test:
    print(item[1])
ls=[1,2,3,4]
one,two=ls[0],ls[1]
print(one)
print(two)
print(ls)
ls.clear()
print(ls)
print(string.digits)
print(type(string.digits))

example='abcdefg'
pattern=re.compile(r'[A-Za-z]')
print(pattern.match(example))
print('\n\n\n\n\n\n\n\n\n')
a_z = re.compile(r'[a-z]')
A_Z = re.compile(r'[A-Z]')
num = re.compile(r'[0-9]')
char = re.compile(r'[$#@]')
test='abcdEF12＃@'
# print(a_z.match(test))
print(A_Z.search(test))
print(num.match(test))
print(char.match(test))