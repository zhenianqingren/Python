# try:
#   block
# except (Exception type):
#   block
# else:
#   block
# finally:
#   block
try:
    num=eval(input("Please Input An Integer"))
    print(num**2)
except:
    print("Format Error")
else:
    print("Normal Execution")
finally:
    print("Programme End")
