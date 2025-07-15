from tkinter import *
from tkinter import messagebox

# Create The Main App Window
age_app = Tk()

# Chaneg App Label
age_app.title("CSeven Calc")

# Set Dimensions
age_app.geometry("600x300")

# Write Label
the_text = Label(age_app, text="Write Your Age", height=2, font=("Arial", 20))
the_text.pack() # Place the Text Into The main Window

# Age Variables
age = StringVar()

# Default Value
age.set("00")

# Calc Function
def calc():

    # Get Age In Years
    the_age_value = age.get()
    
    # Get Time Units
    months = int(the_age_value) * 12
    weeks = months * 4
    days = int(the_age_value) * 365

    line_one = f"Your Age In Months Is : {months}" 
    line_two = f"Your Age In Weeks Is : {weeks}"
    line_three = f"Your Age In Days Is : {days}"

    all = [line_one, line_two, line_three]

    messagebox.showinfo("Your Age In All Time Units", "\n".join(all))

#Create The Input
age_input = Entry(age_app, width=2, font=("Arial", 30), textvariable=age)
age_input.pack() # Place the Input Into The main Window

# Create The Calculate Button
calc_button = Button(age_app, text="Calculate", 
                     width=20, 
                     height=2, 
                     bg="#99d875", 
                     fg="#2f3f05", 
                     borderwidth=0,
                     command=calc)

calc_button.pack() # Place the Button Into The main Window

# Run App

age_app.mainloop()
