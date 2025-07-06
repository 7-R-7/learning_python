Tuple = ("HTML", "CSS", "JS")

user_skills = {
    "PHP" : "70%",
    "C++" : "80%",
    "Python" : "90%"
}

def show_skills (name, *skills, **progress):
    print(f"Hello {name} \nSkills without progress are :")
    for skill in skills:
        print (f"- {skill}")
    print ("Skills with progress are :")

    for skill_key, skill_value in progress.items():
        print (f"- {skill_key} => {skill_value}")

show_skills ("CSeven", *Tuple, **user_skills)
