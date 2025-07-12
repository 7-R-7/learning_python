students = {
    "Mohamed" : {
        "Network" : "50%",
        "Dev Web" : "90%",
        "Linux" : "70%"
    },
    "Mustapha" : {
        "Network" : "90%",
        "Dev Web" : "40%",
        "Linux" : "80%"
    },
    "Ahmed" : {
        "Network" : "70%",
        "Dev Web" : "60%",
        "Linux" : "60%"
    }
}

for name in students :
    print(f"Skills and progress for {name} are :")
    for skill in students[name] :
        print(f"{skill} = {students[name][skill]}")
