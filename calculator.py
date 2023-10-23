from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
            scvalue.set(value)
            screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root=Tk()
root.geometry("600x900")
root.title("Calculator By M.Saad Nomani")
root.wm_iconbitmap('calculator.png')
root.configure(bg="black",borderwidth=10,relief=SUNKEN)

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="Lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(root,bg="grey")
b=Button(f,text="9",padx=28,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=28,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=28,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
f.pack()
f=Frame(root,bg="grey")
b=Button(f,text="6",padx=28,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=28,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
b=Button(f,text="4",padx=28,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
f.pack()
f=Frame(root,bg="grey")

b=Button(f,text="3",padx=28,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=28,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
b=Button(f,text="1",padx=28,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
f.pack()
f=Frame(root,bg="grey")

b=Button(f,text="0",padx=28,pady=2,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
b=Button(f,text="-",padx=28,pady=3,font="Lucida 40 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
b=Button(f,text="*",padx=33,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
f.pack()
f=Frame(root,bg="grey")

b=Button(f,text="/",padx=22,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
b=Button(f,text="%",padx=28,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
b=Button(f,text="C",padx=28,pady=3,font="Lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
f.pack()
f=Frame(root,bg="grey")

b=Button(f,text="=",padx=28,pady=3,font="Lucida 35 bold",bg="Black",fg="White")
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()
