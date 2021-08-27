print(0.2+0.1==0.3)
# There is an indefinite mantissa in the decimal of the computer
print(round(0.1+0.2,1)==0.3)
# round(x,d) x represents data and d represents the number of bits intercepted

# complex number

# operator

print(10/3)
# rounding
print(10//3)
# exponentiation
print(10**3)
# when the right is decimal, it belongs to square operation
print(10**0.3)
# when different types of data are mixed, the result data type is the maximum type
# complex number>floating point number>integer
print(100+0.3)

# numerical operation function
# abs(x) take absolute value
# divmod(x,y) output quotient and remainder at the same time. For example, if the input is (10,3), the output is (3,1)
# pow(x,y[,z]) power remainder (x**y%10000)  [..]indicates that the parameter Z can be omitted
# int(x) Case: int(123.45)->123 int("123")->123
# float(x) Case: float(12)->12.0
print(complex(10))
print(float("123"))