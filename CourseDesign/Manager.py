import jieba
import tkinter.messagebox
import wordcloud


class manager:
    def __init__(self):
        self.List = None
        self.content = None
        self.Dict = None
        self.PictureManager = None

    def get_content(self):
        return self.content

    def split_Text(self, Text):
        self.content = jieba.lcut(Text)

    def get_List(self):
        return self.List

    def Address_Add(self, ls_add):#向已有的List中插入要添加的分词，原理即将新添加的分词的次数设置为已有分词的最大次数，保证其出现在词云中
        if (len(ls_add) == 0):
            return
        else:
            max = self.get_List()[0][1]
            for key in ls_add:
                if len(key) <=1 or key.isspace():
                    continue
                if (key,max) in self.List:
                    tkinter.messagebox.showwarning(title='警告', message='要添加的词" ' + key + ' "已经存在')
                else:
                    self.List.insert(0, tuple((key, max)))

    def Address_Del(self, ls_del):#删除分词,即将分词次数置0
        if (len(ls_del) == 0):
            return

        for char in ls_del:
            if len(char)<=1 or char.isspace():
                continue
            if self.Dict.get(char, -1) != -1:
                self.Dict.pop(char, 0)
            else:
                tkinter.messagebox.showwarning(title='警告', message='要删除的词" ' + char + ' "不存在')

    def Write_List(self):#将分词结果写入csv文件中，微软产品默认gbk编码，因此第一个写入utf-8编码便于下一次可能的导入，第二个写入gbk编码方便用户查看
        with open('split_word.csv', 'w', encoding='utf-8') as fp:
            for word, count in self.List:
                fp.write(word + ',' + str(count) + '\n')
        with open('split_word_show.csv', 'w', encoding='gbk') as fp_show:
            for word, count in self.List:
                fp_show.write(word + ',' + str(count) + '\n')

        tkinter.messagebox.showinfo(title='提示',message='导入成功')

    def get_Dict(self, file_path):#生成词典 key:分词 value:次数
        Dict = {}
        if file_path == 'default' and self.content != None:
            for char in self.content:
                if (len(char) <= 1 or char in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~·‘’《》\n\t\b'):
                    continue
                else:
                    Dict[char] = Dict.get(char, 0) + 1
        elif file_path != 'default':
            csv_file = open(file_path, 'r', encoding='utf-8')
            for line in csv_file:
                ls = (line.replace('\n', '')).split(',')
                if (len(ls) < 2):
                    continue
                Dict[str(ls[0])] = int(ls[1])
            csv_file.close()

        return Dict

    def generate_split_word(self, Text, ls_add, ls_del, file):
        if (len(Text) > 1):
            self.split_Text(Text)
            self.Dict = self.get_Dict('default')
        else:
            self.Dict = self.get_Dict(file)

        if(len(self.Dict)<=0 or self.Dict==None):
            tkinter.messagebox.showwarning(title='警告', message='请输入有效文本')
            return

        self.Address_Del(ls_del)

        self.List = list(self.Dict.items())
        self.List.sort(key=lambda x: x[1], reverse=True)

        self.Address_Add(ls_add)

    def build_picture(self, font, wid, hei, max_w, shape, bk='black'):#生成词云

        self.PictureManager = wordcloud.WordCloud(font_path=font, \
                                                  width=wid, height=hei, background_color=str(bk), \
                                                  max_words=max_w, mask=shape)

        Dict_copy = dict(self.get_List())
        self.PictureManager.generate_from_frequencies(Dict_copy)
        self.PictureManager.to_file("Report.png")
