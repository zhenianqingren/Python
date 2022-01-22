import os

print('\n\n\n')
print(os.path.abspath("OS.py"))
# print(os.path.normpath("D:\\TempLearn"))
# print(os.path.relpath("D:\data_structure"))

# print(os.path.dirname("D:\\python\\project1\\ProgrammingMethod\\OS.py"))
# print(os.path.basename("D:\\python\\project1\\ProgrammingMethod\\OS.py"))
# print(os.path.join("D:\\","python\\project1\\ProgrammingMethod\\OS.py"))

print(os.path.exists("D:\\NoExists"))
print(os.path.isdir("D:\\TempLearn"))
print(os.path.isfile("file.txt"))

# print(os.system("D:\\TempLearn\\bin\\EightQueens.exe"))

print(os.getlogin())
print(os.cpu_count())