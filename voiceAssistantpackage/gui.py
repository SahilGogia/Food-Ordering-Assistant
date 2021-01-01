from tkinter import *
from PIL import Image, ImageTk


root = Tk()

C = Canvas(root, height=950, width=500)
C.pack()
fimage = Image.open('bg.jpg')
photo_image = ImageTk.PhotoImage(fimage)
background_label = Label(root, image=photo_image)
background_label.place(relwidth=1, relheight=1)


b = Button(root,text = "Activate",borderwidth=-10)

b.pack()



root.mainloop()
