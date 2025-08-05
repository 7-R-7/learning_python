# label = an area widget that hold text and/or an image within a window
from tkinter import *

window = Tk()

logo = PhotoImage(file="icons/logo.png")

label = Label(window, 
              text="Hello from CSeven", 
              font=('Arial',40,'bold'), 
              fg="#f8833f",           # fg -> foreground 
              bg='black',               # bg -> background
              relief=RAISED,            # relief -> border style
              bd = 10,                  # bd -> border
              padx=20,                  # padx -> padding x
              pady=20,                  # pady -> padding y
              image=logo,
              compound= 'bottom'         # position of image
            )            
label.pack()

#label.place(x=100, y=100) # position of label same as pack



window.mainloop()
