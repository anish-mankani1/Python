from tkinter import *
root=Tk()
root.title("hi")
root.geometry('300x400')
def gui():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0

lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"hi anish how are you")
lbx.insert(END,"hi anish how are you")
b1=Button(root,text="submit",command=gui).pack()
root.mainloop()