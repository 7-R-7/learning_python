from tkinter import *

window = Tk()

fireIcon = PhotoImage(file='icons/fire.png')
fireLabel = Label(image=fireIcon)
fireLabel.pack()

def submit():
    print("The temperature is : " + str(scale.get()) + " C°")

scale = Scale(window, 
              from_=100, 
              to=0,
              length=600,
              orient=VERTICAL,
              font = ('Consolas',18),
              tickinterval=10, # adds numeric indicators ofr value
              #showvalue=0 #hide current value
              #resolution=5 #increment of slider
              troughcolor="#ff0080",
              fg="#0b0377",
              bg="#f6ab08"
              )
scale.set((scale['from']-scale['to'])/2)
scale.pack()

snowIcon = PhotoImage(file='icons/snow.png')
snowLabel = Label(image=snowIcon)
snowLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()