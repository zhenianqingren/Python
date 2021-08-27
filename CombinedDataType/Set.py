# elementS in the set cannot be changed
# elements in the set are not duplicated
A={"python",123,("python",123)}
B=set("python123python123")
C={"python",123,"python",123}
print(A)
print(B)
print(C)

# operator
# S | T union of S and T
# S - T elements in set S but not in set T
# S & T intersection of S and T
# S ^ T different elements of S and T
# S <= T or S < T return True/False,judge the subset relationship between S and T
# S >= T or S > T return True/False,judge the inclusion relationship between S and T

# method
# S.add(x) If x is not in S, add x to S
# S.discard(x) remove x frome S ,If x is not in S, not warn exception
# S.remove(x) remove x frome S ,If x is not in S, warn KeyError exception
# S.clear() delete all elements
# S.pop() like stack, take an element randomly from S and return for user
# S.copy() return a copy of S
# len(S) number of elements
# x in S (True/False) <-> x not in S
# set(x) Convert variable x of other types to set
A={"python",123,"Java"}
try:
    while True:
        print(A.pop())
except:
    pass













