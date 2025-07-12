import re

email_input = input("Please Write Your Email : ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

email_list = []

if search != []:
    email_list.append(search)

    print("Email Added !")

else :

    print("Invalid Email")

for email in email_list:
    print(email)
