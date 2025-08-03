from tkinter import *

count = 0

def click():
    global count
    count += 1
    label.config(text=count)

window = Tk()

button = Button(window,text="Click Me !")

button.config(command=click) # performs call back of function

button.config(font=('Ink Free', 50, 'bold'))

button.config(bg="red")

button.config(fg="yellow")

button.config(activebackground="blue") # when click on button

button.config(activeforeground="white") # when click on button

picture = PhotoImage(file="button.png")

button.config(image= picture)

button.config(compound='bottom')

#button.config(state= DISABLED) # disabled button 

label = Label(window, text=count)

label.config(font=('Monospace',50))

label.pack()

button.pack()

window.mainloop()