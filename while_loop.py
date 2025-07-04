students = ["Mohamed", "Ahmed", "Mustapha", "Omar", "Ali"]

a = 0

while a < len(students):
    print (f"#{str(a+1).zfill(3)} {students[a]}") # I added a+1 so the counting start with 1 not 0
    a +=1
print("*End*")
