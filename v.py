from tkinter import *
root=Tk()
root.title("calculator")
root.geometry("1000x3000")

def click(event):
    global s
    text=event.widget.cget("text")
    print(text)
    if(text == "="):
        if(s.get().isdigit()):
            value=int(s.get())
        else:
            value=eval(screen.get())
        s.set(value)
        screen.update()
    elif(text == "AC"):
        s.set("")
        screen.update()
    else:
        s.set(s.get()  +  text)
        screen.update()


s=StringVar()
s.set("")

Label(root,text="Welcome to the  Anish 's Calculator",font="Lucida 19 bold ",fg="purple").pack()
Label(root,text="Please use Calculator to perform Calculations",font="Lucida 19 bold ",fg="Blue").pack()


screen=Entry(root,textvariable=s,font="Lucida 19 bold")
screen.pack(padx=20,pady=20,fill=X,ipadx=9)

f=Frame(root,bg="grey")
b=Button(f,text="9",font="Lucida 19 bold",padx=20,pady=5)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="Lucida 19 bold",padx=20,pady=5)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="7",font="Lucida 19 bold",padx=20,pady=5)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="6",font="Lucida 19 bold",padx=20,pady=19)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="Lucida 19 bold",padx=20,pady=18)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="4",font="Lucida 19 bold",padx=20,pady=18)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="3",font="Lucida 19 bold",padx=20,pady=18)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="Lucida 19 bold",padx=20,pady=18)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="1",font="Lucida 19 bold",padx=20,pady=18)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="+",font="Lucida 19 bold",padx=22,pady=18)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="Lucida 19 bold",padx=22,pady=18)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="*",font="Lucida 19 bold",padx=22,pady=18)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="/",font="Lucida 19 bold",padx=21,pady=18)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="%",font="Lucida 19 bold",padx=21,pady=18)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="Lucida 19 bold",padx=21,pady=18)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="AC",font="Lucida 19 bold",padx=18,pady=19)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text=".",font="Lucida 19 bold",padx=18,pady=19)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="^",font="Lucida 19 bold",padx=18,pady=19)
b.pack(padx=15,pady=5,side=LEFT)
b.bind("<Button-1>",click)

f.pack()



root.mainloop()
