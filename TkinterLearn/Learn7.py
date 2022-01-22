import tkinter as tk  # 使用Tkinter前需要先导入

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')


# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

# 第4步，place 放置方法（精准的放置到指定坐标点的位置上）
l=tk.Label(window, text='Pl', font=('Arial', 10),bg='green')
l.place(x=245,y=145,anchor='nw',height=10,width=10)

# 第5步，主窗口循环显示
window.mainloop()