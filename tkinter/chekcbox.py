from tkinter import *

def display():
    if (x.get() == 1) & (y.get()==0):
        print("Follow CSeven")
    if (x.get() == 0) & (y.get()==1):
        print("Follow 7-R-7")
    if (x.get() == 1) & (y.get()==1):
        print("Follow both Cseven & 7-R-7")
    else:
        print("Unfollow")
window = Tk()

x = IntVar()

y = IntVar()

checkbox = Checkbutton(window,text='CSeven',variable=x,onvalue=1,offvalue=0,command=display)

checkbox.pack()

checkbox.config(font=("Arial",30)) 

checkbox.config(fg="#ee2303")

checkbox.config(bg="#060f71")

checkbox.config(activeforeground="#ee2303")

checkbox.config(activebackground="#060f71")

photo = PhotoImage(file='mini.png')

checkbox.config(image=photo,compound=LEFT)

checkbox.config(padx=25, pady=20,width=250,height=50)

checkbox.config(anchor='w') # anchors widget to relative cardinal  direction

checkbox2 = Checkbutton(window,text='7-R-7',variable=y,onvalue=1,offvalue=0,command=display)

checkbox2.pack()

checkbox2.config(font=("Arial",30)) 

checkbox2.config(fg="#ee2303")

checkbox2.config(bg="#060f71")

checkbox2.config(activeforeground="#ee2303")

checkbox2.config(activebackground="#060f71")

photo2 = PhotoImage(file='mini.png')

checkbox2.config(image=photo2,compound=LEFT)

checkbox2.config(padx=25, pady=20,width=250,height=50)

checkbox2.config(anchor='w') # anchors widget to relative cardinal  direction


window.mainloop()