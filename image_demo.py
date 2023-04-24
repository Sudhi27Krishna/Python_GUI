from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("300x400") # to set the window size (width x height)
image = Image.open("2bddc91accccb9b70178c49cf5684bed.jpg")
photo = ImageTk.PhotoImage(image)
image_label = Label(image=photo)
image_label.pack()
root.mainloop()