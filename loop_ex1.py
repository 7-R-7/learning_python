mySkills = {
    "Network" : "90%",
    "Web Dev" : "70%",
    "Mobile Dev" : "60%",
    "Linux" : "80%",
    "Windows" : "90%"
}
print("Here is my progress in each field :")
for skill in mySkills :
    print(f"{skill} = {mySkills.get(skill)}")
