# radio button = similar to checkbox , but you can only select one from a group

from tkinter import *

food = ["pizza","cheeseburger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza !")
    elif(x.get()==1):
        print("You ordered cheeseburger")
    elif(x.get()==2):
        print("You ordered cheeseburger")
    else:
        print("Yo kid stop !")
window = Tk()

pizzaImage = PhotoImage(file="icons/pizza.png")
cheeseburgerImage = PhotoImage(file="icons/cheeseburger.png")
hotdogImage = PhotoImage(file="icons/hotdog.png")

foodImage = [pizzaImage, cheeseburgerImage, hotdogImage]

x = IntVar()

for index in range (len(food)):
    radiobutton = Radiobutton(  window, 
                                text=food[index],  # adds text to radio button
                                variable=x,        # groups radiobuttons together if they share same variable
                                value=index,       # assigns each radiobutton a different value
                                padx= 25,
                                font = ("Impact",50),
                                image = foodImage[index],# adds image to radiobutton
                                compound='left',  # adds image and text (left-side)
                                indicatoron = 0, # eliminate circle indicators
                                width=550, # sets width of radio buttons
                                command=order) # set command of radiobutton to function
    radiobutton.pack(anchor=W)

window.mainloop()