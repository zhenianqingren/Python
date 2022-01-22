import tkinter

window=tkinter.Tk()

window.title('My Window')

window.geometry('960x720')

var=tkinter.StringVar()

winlabel=tkinter.Label(window,textvariable=var,bg='#BBFFFF',font=('Arial',12),width=30,height=2)

winlabel.pack()

on_hit=False
def hit_me():
    global on_hit
    if on_hit:
        on_hit=False
        var.set(' ')
    else:
        on_hit=True
        var.set('You hit me')

winbutton=tkinter.Button(window,text='hit me',bg='white',font=('Arial',12),width=10,height=2,command=hit_me)
winbutton.pack()

winEntry=tkinter.Entry(window,show=None,font=('Arial',14))
winEntry.pack()

window.mainloop()