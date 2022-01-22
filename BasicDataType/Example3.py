
# There are 365 days in a year. The progress is 1% every day. What is the cumulative progress
# There are 365 days in a year, with a 1% step back every day. How much is left
print("{:.2f} {:.2f}".format(1.01**365,0.99**365))
# working days improve, weekends retreat

day=1.0
dayfactor=0.1
for i in range(1,366):
    if i%7 in [0,6]:
        day=day*(1-dayfactor)
    else:
        day=day*(1+dayfactor)
print("{:.2f}".format(day))

# To what extent does the workday model work as hard as 1% every day?
def DayUp(df):
    result=1
    for i in range(1,366):
        if i%7 in [0,6]:
            result=result*(1-df)
        else:
            result=result*(1+df)
    return result
factor=0.01
while round(DayUp(factor),3)<=37.78:
    factor+=0.0001
print("{:.3f}".format(factor))





















