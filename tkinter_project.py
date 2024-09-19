from tkinter import *
from PIL import image,ImageTk
mahmudul_root = Tk()
mahmudul_root.geometry("1255x944")


#photo = PhotoImage(file="C:\Users\Anish mankani\OneDrive\Pictures")
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
#varun_label = Label(mahmudul_root,image=photo)
#varun_label.pack()
image=image.open("1.png")


varun_label =Label(mahmudul_root,image=photo)
varun_label.pack()
mahmudul_root.configure()



mahmudul_root.mainloop()