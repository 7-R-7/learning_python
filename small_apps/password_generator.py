import string 
import random

def make_serial(count):
    
    all_chars = string.ascii_letters + string.digits + string.punctuation 

    chars_count = len(all_chars)

    serial_list = []

    while count > 0:

        random_number = random.randint(0, chars_count - 1)

        random_character = all_chars[random_number]

        serial_list.append(random_character)

        count -= 1

    return("".join(serial_list))

user_psk = input("Enter the length of the password : ")
try: 
    user_psk = int(user_psk)
    final_psk = make_serial(int(user_psk))
    print(f"Your Password is : ( {final_psk} )")
except :
    print("Wrong ! Only Numbers Are Allowed")
