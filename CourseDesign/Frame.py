import copy
import tkinter
import tkinter.ttk
import Items
import Manager
import tkinter.filedialog
import os
from imageio import imread


# 提示对话框
# 异常对话框
# 词云参数
class Frame:
    window = tkinter.Tk()#窗口
    menubar = tkinter.Menu(window)#菜单栏
    items = Items.items()#控件

    frame_left_up = tkinter.Frame(window, borderwidth=2, relief="groove")#左上界面
    frame_left_down = tkinter.Frame(window, borderwidth=2, relief="groove")#左下界面
    frame_right = tkinter.Frame(window, borderwidth=2, relief="groove")#右部界面

    manager = Manager.manager()#文本处理

    # 初始化
    def __init__(self):
        self.window.title('词云生成器')
        self.window.geometry('1440x720')

        self.Menubar_init()
        self.frame_left_up_init()
        self.frame_left_down_init()
        self.frame_right_init()

        self.font_path = 'msyh.ttc'#词云字体路径默认值
        self.shapeOfphoto=None#词云形状
        self.width=960#宽度
        self.height=720
        self.max_words=30#最大显示词数
        self.read_csv='default'
        self.write_csv=None
        self.place_background_color()

    # 菜单栏的初始化
    def Menubar_init(self):
        self.menubar.add_command(label='生成分词', command=self.show_split_word)
        self.menubar.add_command(label='生成词云', command=self.generate_png)
        self.menubar.add_command(label='退出', command=self.window.quit)
        self.menubar.add_command(label='导入csv文件',command=self.import_csv)
        self.menubar.add_command(label='写入csv文件',command=self.write_csv)

        self.window.config(menu=self.menubar, bg='#F5FFFA')

    # 增加词语与删除词语框的初始化
    def frame_left_up_init(self):
        self.frame_left_up.place(x=0, y=0, width=432, height=216)
        self.items.Text_add = tkinter.Text(self.frame_left_up, font=('Arial', 14), relief='groove', wrap='word')
        self.items.Text_decre = tkinter.Text(self.frame_left_up, font=('Arial', 14), relief='groove', wrap='word')

        self.items.Text_add.place(x=0, y=20, width=202, height=186)
        self.items.Text_decre.place(x=216, y=20, width=209, height=186)

        self.items.Text_add.insert(1.0, '每行请输入一个词语')
        self.items.Text_decre.insert(1.0, '每行请输入一个词语')

        self.AddScroll(self.items.Text_add)
        self.AddScroll(self.items.Text_decre)#添加滚动控件

        self.AddDescription(0, 0, '增加词语', self.frame_left_up)
        self.AddDescription(216, 0, '删除词语', self.frame_left_up)

    # 增加滚动条
    def AddScroll(self, Text):
        scroll = tkinter.Scrollbar(Text, command=Text.yview)
        Text['yscrollcommand'] = scroll.set
        scroll.pack(side='right', fill='y')

    # 添加信息描述
    def AddDescription(self, x, y, text, frame):
        label = tkinter.Label(frame, text=text, anchor='w')
        label.place(x=x, y=y, width=100, height=20)

    # 源文本部分的初始化
    def frame_left_down_init(self):
        self.frame_left_down.place(x=0, y=222, width=432, height=495)
        self.items.Text_src = tkinter.Text(self.frame_left_down, font=('Arial', 14), relief='groove', wrap='word')
        self.items.Text_src.place(x=2, y=22, width=420, height=460)

        self.AddScroll(self.items.Text_src)
        self.AddDescription(0, 2, '源文本', self.frame_left_down)
        import_text = tkinter.Button(self.frame_left_down, text='导入文本', command=self.import_file)
        import_text.place(x=350, y=0, width=70, height=22)

    # 结果界面的初始化
    def frame_right_init(self):
        self.frame_right.place(x=437, y=0, width=1000, height=717)
        self.items.tabBar = tkinter.ttk.Notebook(self.frame_right)
        self.items.tabBar.place(x=0, y=0, width=996, height=713)

        self.items.tab1 = self.AddTab(self.items.tabBar, '分词')
        self.items.tab2 = self.AddTab(self.items.tabBar, '词云')

        self.items.word_split = tkinter.Text(self.items.tab1, font=('Arial', 14), relief='groove', wrap='word')
        self.AddScroll(self.items.word_split)
        self.items.word_split.place(x=5, y=5, width=990, height=710)
        self.set_tab2()

    # 设置词云的配置
    def set_tab2(self):
        labelset = tkinter.Label(self.items.tab2, text='设置', anchor='w')
        labelset.place(x=0, y=0, width=995)

        label_wordsnum=tkinter.Label(self.items.tab2,text='设置最大词数(默认为30)',anchor='w')
        label_wordsnum.place(x=0,y=250,width=300)

        select_font = tkinter.Button(self.items.tab2, text='选择字体', command=self.select_font)
        select_font.place(x=0, y=20, width=200, height=200)

        select_shapeOfphoto=tkinter.Button(self.items.tab2,text='选择形状',command=self.set_shapeOfphoto)
        select_shapeOfphoto.place(x=210,y=20,width=200,height=200)

        self.scaleOfwords_num=tkinter.Scale(self.items.tab2,from_=20,to=80,orient=tkinter.HORIZONTAL)
        self.scaleOfwords_num.place(x=0,y=280,width=300,height=45)

        confirmWordsNum=tkinter.Button(self.items.tab2,text='确认',command=self.set_max_words)
        confirmWordsNum.place(x=305,y=295,width=30,height=25)

    def place_background_color(self):
        color_label=tkinter.Label(self.items.tab2,text='请选择背景颜色',anchor='w')#west
        color_label.place(x=0,y=330,width=180,height=45)
        self.bk_var=tkinter.StringVar()

        black=tkinter.Radiobutton(self.items.tab2,text='black',variable=self.bk_var,value='black',command=self.print_selection)
        black.place(x=0,y=380,width=80,height=45)

        white=tkinter.Radiobutton(self.items.tab2,text='white',variable=self.bk_var,value='white',command=self.print_selection)
        white.place(x=0,y=430,width=80,height=45)

        red=tkinter.Radiobutton(self.items.tab2,text='red',variable=self.bk_var,value='red',command=self.print_selection)
        red.place(x=0,y=480,width=80,height=45)

        yellow=tkinter.Radiobutton(self.items.tab2,text='yellow',variable=self.bk_var,value='yellow',command=self.print_selection)
        yellow.place(x=0,y=530,width=80,height=45)
    # 导入csv文件,即导入路径
    def import_csv(self):
        csv_path=str(os.path.abspath(tkinter.filedialog.askopenfilename()))
        if csv_path.split('.')[-1]!='csv':
            tkinter.messagebox.showerror(title='错误',message='请导入符合格式的csv文件')
        else:
            try:
                test=open(csv_path,'r',encoding='utf-8')
                s=test.read()
                self.read_csv=csv_path
                test.close()
                tkinter.messagebox.showinfo(title='提示',message='导入成功')
            except Exception:
                tkinter.messagebox.showerror(title='错误',message='请导入utf-8编码的csv文件')
    # 将结果写入csv文件
    def write_csv(self):
        src_split_words=self.items.word_split.get('2.0','end')
        if(len(src_split_words)<=2):
            tkinter.messagebox.showerror(title='错误',message='请生成有效分词')
            return
        self.manager.Write_List()

    def print_selection(self):
        tkinter.messagebox.showinfo(title='提示',message="you've chosen "+self.bk_var.get())
    # 选择字体
    def select_font(self):
        font_path = str(os.path.abspath(tkinter.filedialog.askopenfilename()))
        print(font_path)
        judge_ls = font_path.split('.')
        suffix = str.lower(judge_ls[-1])
        if (suffix != 'ttf' and suffix != 'ttc'):
            tkinter.messagebox.showerror(title='错误', message='请导入符合格式的字体文件')
        else:
            self.font_path = font_path
            tkinter.messagebox.showinfo(title='提示', message='导入成功')

    # 设置分词与词云的tab
    def AddTab(self, tabBar, text):
        tab = tkinter.Frame(tabBar)
        tab.place(x=0, y=0, width=1000, height=717)
        tabBar.add(tab, text=text)
        return tab

    # 导入文本文件
    def import_file(self):
        try:
            path = tkinter.filedialog.askopenfile(title='请导入utf-8编码文本文件')
            file = open(path.name, encoding='utf-8')
            text = file.read()
            file.close()
            self.items.word_split.delete('1.0', 'end')
            self.items.Text_src.insert('1.0', text)
        except Exception:
            tkinter.messagebox.showerror(title='警告', message='请导入utf-8编码文本文件')
        finally:
            pass

    # 展示分词
    def show_split_word(self):
        self.items.word_split.delete('1.0', 'end')

        src_text = self.items.Text_src.get('1.0', 'end')
        self.manager.generate_split_word(src_text, self.Add_word(), self.Del_word(),self.read_csv)

        Show = self.manager.get_List()

        if Show == None or len(Show)==0:
            tkinter.messagebox.showwarning(title='提示', message='请输入有效文本')
        else:
            index = 2.0
            self.items.word_split.insert(1.0, '词语 : 出现次数\n')
            for i in range(len(Show)):
                word, count = Show[i]
                if count > 0:
                    self.items.word_split.insert(index, word + ' : ' + str(count) + '\n')
                    index += 1

    # 添加分词
    def Add_word(self):
        txt = self.items.Text_add.get(2.0, 'end')

        if len(txt) <= 0:
            return []

        ls = txt.split('\n')
        del ls[-1]
        return ls
    # 删除分词
    def Del_word(self):
        txt = self.items.Text_decre.get(2.0, 'end')

        if len(txt) <= 0:
            return []

        ls = txt.split('\n')
        del ls[-1]
        return ls

    # 设置背景样式
    def set_shapeOfphoto(self):
        shape_path = str(os.path.abspath(tkinter.filedialog.askopenfilename()))
        print(shape_path)
        judge_ls = shape_path.split('.')
        suffix = str.lower(judge_ls[-1])
        if (suffix != 'jpg' and suffix != 'png'):
            tkinter.messagebox.showerror(title='错误', message='请导入".png"或".jpg"格式的文件')
        else:
            self.shapeOfphoto = imread(shape_path)
            tkinter.messagebox.showinfo(title='提示', message='导入成功')

    def set_max_words(self):
        self.max_words=self.scaleOfwords_num.get()
        tkinter.messagebox.showinfo(title='提示',message='显示最大词数已设置为'+str(self.max_words))


    # 生成词云
    def generate_png(self):
        src_text = self.items.Text_src.get('1.0', 'end')
        self.manager.generate_split_word(src_text, self.Add_word(), self.Del_word(),self.read_csv)

        if (len(self.manager.get_List()) <= 0):
            tkinter.messagebox.showwarning(title='提示', message='请输入文本')
            return

        try:
            self.manager.build_picture(self.font_path,self.width,self.height,self.max_words,self.shapeOfphoto,self.bk_var.get())
        except Exception:
            tkinter.messagebox.showerror(title='错误',message='非法参数')
            return
        tkinter.messagebox.showinfo(title='提示', message='图片生成完毕')


myframe = Frame()
myframe.window.mainloop()
