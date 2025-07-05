webs_list = []

list_size = 5

while list_size > 0 :
    website = input ("Enter The name of your website without https :").strip().lower()
    webs_list.append(f"https://{website}")
    list_size -=1
    if list_size > 1 :
        print(f"Website added , {list_size} places left")
    else :
        print(f"Website added , {list_size} place left")
else :
    print("Your List is full !")
    print("Here is the list of the added websites :")
    for web in webs_list :
        print(f"#{webs_list.index(web)+1} {web}")
