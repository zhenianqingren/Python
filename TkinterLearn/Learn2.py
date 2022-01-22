import tkinter

window=tkinter.Tk()

window.title("My Window")

window.geometry('962x720')

winEntry=tkinter.Entry(window,show=None)
winEntry.pack()

winText=tkinter.Text(window,height=3)

def insert_point():
    var=winEntry.get()
    winText.insert('insert',var)

def insert_end():
    var=winEntry.get()
    winText.insert('end',var)

winButton1=tkinter.Button(window,text='insert point',width=10,height=2,command=insert_point)
winButton2=tkinter.Button(window,text='insert end',width=10,height=2,command=insert_end)

winButton1.pack()
winButton2.pack()

winText.pack()

window.mainloop()