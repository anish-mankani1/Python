from tkinter import *
root=Tk()
root.title("hey anish")
root.geometry('400x700')

def getval():
    print(f"ordered is placed{var.get()}")

var=StringVar()
var.set("radio")

Label(root,text="welcome to harrys kitchen",font="Lucida 19 bold").pack()
Radiobutton(root,text="Dosa",variable=var,value="dosa").pack(anchor="w")
Radiobutton(root,text="Idly",variable=var,value="idly").pack(anchor="w")
Radiobutton(root,text="Samosa",variable=var,value="samosa").pack(anchor="w")
Radiobutton(root,text="Samarvada",variable=var,value="samarwada").pack(anchor="w")

Button(root,text="submit",command=getval).pack()

root.mainloop()