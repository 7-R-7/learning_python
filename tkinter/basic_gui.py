# widgets = GUI elements : buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

from tkinter import *

window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title("Basic GUI")

logo = PhotoImage(file='icons/logo.png')
window.iconphoto(True,logo)
window.config(background="#9CF1DF")


window.mainloop() # place window on computer screen , listen for events