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