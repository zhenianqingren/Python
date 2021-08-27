# Representation of string
# Single quotation marks represent a single line string
A = 'This is a line of string'
# Double quotation marks represent a single line string
B = "This is a line of string"
# Three single quotes or three double quotes represent a multiline string
C = '''This is
a multiline string
'''

print(A)
print(B)
print(C)

# There are quotation marks in the string content
print("There are single quotes here ' ' ' ")
print('There are double quotes here " " " ')
print('''There are single quotation marks as well as double quotation marks ' ' " "''')

# Use [] to get one or more characters in a string The inside of [] is an index
# positive increment sequence number  The first index is 0
# reverse decrement sequence number The last index is - 1

# <string>[M:N], M missing indicates to the beginning and N missing indicates to the end
# indicates that take characters with index from M to N-1
# <string>[M:N:K] slice the string according to the length of step of K Case: "0123456789"[1:6:2]=135
# Case: <string>[::-1] indicates that reverse the string
# escape character:\
print("0123456789"[::-1])

# operator
M="abc"
N="def"
O=M+N
print(O)
print(5*O)
print(M in O)

# string-handling functions
# len(x) return the length of x
# str(x) return string form corresponding to any type x
print(len(str(123)))

# hex(x) or oct(x) hexadecimal string or octal string of integer x
print(hex(425))

# chr(u) u is Unicode encoding. It will return its corresponding character
# ord(x) x is a character. It will return its corresponding Unicode encoding
print(ord("a"))

# Tips: print(……,end="") when the content of end is empty, print won't wrap


# string processing method
# str.lower() // str.upper() returns a copy of str in all uppercase or lowercase
print("ABCdef".lower())

# str.split(sep=None)
print("A,B,C".split(','))
# str.count(sub) returns the number of times of occurrences of sub in str

# str.replace(old,new) returns a copy of str, and all old are replaced with new
# str.center(width[,fillchar])
print("Python".center(16,'-'))
print("Python".center(16))
# str.strip(chars) remove the listed characters that appear on the left and right from str
print("=  Python=".strip(" =nP"))
# str.join(iter) return string
print(",".join('123456'))


# formatting of string types
# Use:<template>.format(<parameters>)

# if not use index, the content of .format appear in default order
print("charater {} corresponds to Unicode {}".format('a',97))
# else
print("Unicode {1} corresponds to character {0}".format('a',97))

# : <fill> <alignment> <width>    <,>(thousands separator for numbers) <.accuracy>(the precision of a floating-point number or the maximum output length of a string) <type>(Integer:b c d o x x Float:e E f %)
print("{:=^20}".format("Python"))
print("{:+<20}".format("Python"))
print("{:->20}".format("Python"))

print("{:,.2f}".format(123456.789))
print("{0:b} {0:c} {0:d} {0:o} {0:x} {0:x}".format(425))
print("{0:e} {0:E} {0:f} {0:%}".format(3.14))








