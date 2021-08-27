# its all method and operator are just like string(in,not in,*,[::])
# len(s) return length of s
# min(s) elements in s should be comparable
# max(s)
# s.index(x)/s.index(x,i,j) return position where x first appears in the [i, j] interval of s
# s.count(x) return the total number of x's appearance


# tuple
# once a tuple is created, it can't be modified
creature="cat","dog","human"
print(creature)
creature=(0x0123,"Java","lua","Ruby")
print(creature)
creature=tuple("Python")
print(creature)
print(creature[::-1])

# list
# when a list is created, it can be modified
# the type of elements in a list can be various
ls=[123,"Python",5.8]
lt=ls
print(lt)
# the operator "=" pass an address instead of creating a new list
# ls[i]=x
# del ls[i]
# del ls[i:j:k] Delete elements between interval [i, j] of ls in steps of K
# ls[i:j:k]=lt
# ls+=lt update ls with elements in lt
# ls *= n
# ls.append(x)
# ls.clear()
# ls.copy()
# ls.insert(i,x)
# ls.pop(i)
# ls.remove(x) (the first appearance)
# ls.reverse()






















