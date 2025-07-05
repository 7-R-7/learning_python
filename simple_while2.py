password = "cseven@123"

tries = 3

while tries > 0 :
    user_pass = input ("Enter you password : ")
    if user_pass == password :
        print("Loged in succesfully")
        break
    else :
        tries -=1
        print("Wrong Password !")
        print(f"{tries} attempts left")
    if tries == 0 :
        print ("Attempts finished")
