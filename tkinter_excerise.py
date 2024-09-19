from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry('300x500')
root.title("hey anish ")

texts=[]
photo=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        texts.append(text)
    image=Image.open(f"{i+1}.jpg")
    photo.append(ImageTk.PhotoImage(image))

f1=Frame(root,width=400,height=600).pack()

root.mainloop()