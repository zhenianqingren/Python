import tkinter

window=tkinter.Tk()

window.title('My window')

window.geometry('960x720')

var1=tkinter.StringVar()
var2=tkinter.StringVar()
var2.set((1,2,3,4))


winLabel=tkinter.Label(window,bg='green',fg='yellow',font=('Arial',12),width=10,textvariable=var1)
winLabel.pack()

winListbox=tkinter.Listbox(window,listvariable=var2)

def print_selection():
    value=winListbox.get(winListbox.curselection())
    var1.set(value)

winButton=tkinter.Button(window,text='print selection',width=15,height=2,command=print_selection)
winButton.pack()

list_items=[11,22,33,44]
for item in list_items:
    winListbox.insert('end',item)

winListbox.insert(1, 'first')  # 在第一个位置加入'first'字符
winListbox.insert(2, 'second')  # 在第二个位置加入'second'字符
winListbox.delete(2)  # 删除第二个位置的字符
winListbox.pack()

window.mainloop()
