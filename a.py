from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        display_image(file_path)
        
def display_image(file_path):
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.photo = photo
    status_label.config(text=f"Image loaded: {file_path}")
    
root = Tk()
root.title("Simple Image Viewer")
text_widget = Text(root, wrap=WORD, height=15, width=35)
open_button = Button(root, text="Open Image", command=open_image)
open_button.pack(padx=20, pady=10)
image_label = Label(root)
image_label.pack(padx=20, pady=20)
status_label = Label(root, text="", padx=20, pady=10)
status_label.pack()
root.mainloop()
