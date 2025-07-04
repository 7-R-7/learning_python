admins = ["Mohamed","Mustapha","Ahmed","Omar"]

#Login
name = input("Please enter your name : ").strip().capitalize()


if name in admins :
    print("Hello mate , Welcome back to the Community")
    print("Do you want to update your name or to delete it ?")
    option = input("Update (U) or Delete (D) :").strip().capitalize()
    if option in ["Update" ,"U"]:
        new_name = input("Enter your new name :").strip().capitalize()
        admins[admins.index(name)] = new_name
        print ("Name Updated")
        print (admins)
    elif option in ["Delete" ,"D"] :
        print("Deleting...")
        admins.remove(name)
        print("You are Deleted")
        print(f"Admins are {admins}")
else :
    print("You are not an admin .")
