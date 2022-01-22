# open(file, mode = ‘r’, buffering = -1, encoding = None, errors = None,
#           newline = None, closefd = True, opener = None)
# file参数指定了被打开的文件名称。
# mode参数指定了打开文件后的处理方式。
# buffering参数指定了读写文件的缓存模式。0表示不缓存，1表示缓存，如大于1则表示缓冲区的大小。默认值是缓存模式。
# encoding参数指定对文本进行编码和解码的方式，只适用于文本模式，可以使用Python支持的任何格式，如GBK、utf8、CP936等等。
num=123
with open('test.txt','w',encoding='utf-8') as fp:
    # fp.write(123) 必须写入字符串
    pass
text = '这是一段测试文本'

#以w+方式创建文件，可读可写
with open('test.txt', 'w+', encoding='utf8') as fp:
    fp.write(text)
    #定位文件指针，在utf8编码中，一个汉字占3个字节
    fp.seek(12)
    #从当前位置开始读取剩余内容
    print(fp.read())
    #重新定位
    fp.seek(12)
    #在当前位置写入新内容，覆盖原有内容
    fp.write('模拟')
    #重新定位
    fp.seek(9)
    #在当前位置写入内容
    fp.write('个')
    #定位到文件尾
    fp.seek(0, 2)
    fp.write('，结束。')
    #定位到文件头
    fp.seek(0)
    print(fp.read())

# 定位文件指针，在utf8编码中，一个汉字占3个字节
