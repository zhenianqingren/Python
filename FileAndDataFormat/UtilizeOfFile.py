# <variable>=open(<filename>,<openmode>)
# filename includes path and name
# openmode:
# r ->onlyread default
# w ->overwrite
# x ->if not exist then create,else warn FileExistError
# a ->append write
# b ->binary form
# t ->text form(default)

# <f>.read(size=-1) read all content
# <f>.readline(size=-1)
# <f>.readlines(hint=-1) read all lines and return a list,each line form an element
File=open("D:\\python\\project1\\Key.txt","r",encoding="utf-8")
txt=File.read();
File.close()
print(txt)

File=open("D:\\python\\project1\\Key.txt","r",encoding="utf-8")
for txt in File.readlines():
    print(txt,end="")
File.close()

File=open("D:\\PythonLearn.txt","a",encoding="utf-8")
File.write("\ntest write\n")
File.writelines(["write","test"])
File.close()

# <f>.seek(offset) 0->begin 1->current 2->end
File=open("D:\\PythonLearn.txt","w+",encoding="utf-8")
File.writelines(["Python","FileWrite","Test"])
File.seek(0)
for txt in File.readlines():
    print(txt)
File.close()