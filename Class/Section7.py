# with open('D:\\src.txt','r',encoding='utf-8') as src,open('D:\\dst.txt','w',encoding='utf-8') as dst:
#     dst.write(src.read())

# fname=open('D:\\src.txt','a+',encoding='utf-8')
# ls=['测试1','测试2','测试3','测试4','测试5']
# for s in ls:
#     fname.write(s+'\n')
# fname.seek(0)#关键
# for line in fname:
#     print(line)
# fname.close()

# s='合肥工业大学HFUT'
# fp=open("D:\\sample.txt",'w')
# fp.write(s)
# fp.close()
#
# fp=open("D:\\sample.txt",'r')
# print(fp.read(3))
# fp.seek(2)
# print(fp.read(1))

# import random
# ls=[str(random.randint(0,50)) for i in range(15)]
# with open('D:\\data.txt','w',encoding='utf-8') as fp:
#     for s in ls:
#         fp.write(s+'\n')
#
# fp.close()
#
# with open('D:\\data.txt','r',encoding='utf-8') as fp:
#     ls=fp.readlines()
# fp.close()
#
# for i in ls:
#     print(i,end='')
# ls.sort(key=int)
# print('\n',len(ls[0]))
# with open('D:\\data.txt','w',encoding='utf-8') as fp:
#     fp.writelines(ls)
# fp.close()

# ls=[str(i) for i in range(10)]
# for f,b in enumerate(ls):
#     print(type(f),type(b))

# fo = open("D:\\price2018.csv", "r",encoding='utf-8')
# ls = []
# for line in fo:
#     line = line.replace("\n","")
#     ls.append(line.split(","))
#     print(ls)
# fo.close()

import pickle

# i = 13000000
# a = 99.056
# s = '中国人民123abc'
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# tu = (-5, 10, 8)
# coll = {4, 5, 6}
# dic = {'a':'apple', 'b':'banana', 'g':'grape', 'o':'orange'}
# data = [i, a, s, lst, tu, coll, dic]
#
# with open('sample_pickle.dat', 'wb') as f:
#     try:
#          pickle.dump(len(data), f) #表示后面将要写入的数据个数
#          for item in data:
#               pickle.dump(item, f)
#     except:
#         print('写文件异常!')        #如果写文件异常则跳到此处执行

# with open('sample_pickle.dat', 'rb') as f:
#     n = pickle.load(f)        #读出文件的数据个数
#     print(n)
#     x = pickle.load(f)
#     print(x)
#     x = pickle.load(f)
#     print(x)
#     x = pickle.load(f)
#     print(x)
#     x = pickle.load(f)
#     print(x)
#     x = pickle.load(f)
#     print(x)
#     x = pickle.load(f)
#     print(x)
#     x = pickle.load(f)
#     print(x)

text = '这是一段测试文本'

#以w+方式创建文件，可读可写
# with open('test.txt', 'w+', encoding='utf8') as fp:
#     fp.write(text)
#     #定位文件指针，在utf8编码中，一个汉字占3个字节
#     fp.seek(12)
#     #从当前位置开始读取剩余内容
#     print(fp.read())
#     #重新定位
#     fp.seek(12)
#     #在当前位置写入新内容，覆盖原有内容
#     fp.write('模拟')
#     #重新定位
#     fp.seek(9)
#     #在当前位置写入内容
#     fp.write('个')
#     #定位到文件尾
#     fp.seek(0, 2)
#     fp.write('，结束。')
#     #定位到文件头
#     fp.seek(0)
#     print(fp.read())

import pickle

# i = 13000000
# a = 99.056
# s = '中国人民123abc'
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# tu = (-5, 10, 8)
# coll = {4, 5, 6}
# dic = {'a':'apple', 'b':'banana', 'g':'grape', 'o':'orange'}
# data = [i, a, s, lst, tu, coll, dic]
#
# with open('sample_pickle.dat', 'wb') as f:
#     try:
#          pickle.dump(len(data), f) #表示后面将要写入的数据个数
#          for item in data:
#               pickle.dump(item, f)
#     except:
#         print('写文件异常!')        #如果写文件异常则跳到此处执行
#
# with open('sample_pickle.dat', 'rb') as f:
#     n = pickle.load(f)        #读出文件的数据个数
#     for i in range(n):
#         x = pickle.load(f)
#         print(x)
with open('D:\\ExtractMp4ForWPF.exe','rb') as fr:
    with open('D:\\pythontest.exe','wb') as fw:
            x=fr.read()
            fw.write(x)
















