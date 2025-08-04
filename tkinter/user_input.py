# entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print(f"Hello {username}")

def delete():
    entry.delete(0,END) # deletes the line of text

def backspace():
    entry.delete(len(entry.get())-1,END) # delete the last character

window = Tk()

submit = Button(window,text='Submit',command=submit)

submit.pack(side = TOP)

delete = Button(window,text='Delete',command=delete)

delete.pack(side = BOTTOM)

backspace = Button(window,text='backspace',command=backspace)

backspace.pack(side = BOTTOM)

entry = Entry()

entry.config(font=('Ink Free', 50))

entry.config(bg="#000000")

entry.config(fg="#E8E517")

# entry.insert(0,'CSeven')

# entry.config(state=DISABLED)

entry.config(width=15) # number of maximum char

# entry.config(show='#') # passowrd 

entry.pack()

window.mainloop()