# Import SQLite Module
import sqlite3

# Create Database And COnnect
db = sqlite3.connect("exercice013.db")
# Create Table

db.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Commit (Save) and Close Method
def commit_and_close():

    # Commit (Save) Changes
    db.commit()

    # Close Database
    db.close()
    print("Database Closed")

# Setting Up The Cursor
cr = db.cursor()

# My User ID
uid = 1 

# Input First Message
input_msg = """
What Do You Want ?
"s" --> Show All Skills
"a" --> Add New Skill
"d" --> Delete A Skill
"u" --> Update Skill Progress
"q" --> Quit The App
Choose Option :
"""

#Input Option Choice
user_input = input(input_msg).strip().lower()

# Command list 
cmd_list = ["s", "a","d","u","q"]

#Methods

def Show_skills():

    cr.execute(f"select * from skills where user_id = '{uid}'")

    results = cr.fetchall()

    print(f"You Have {len(results)} Skills")

    if len(results) > 0 :
        print("Showing Skills With Progress : ")

    for row in results :

        print(f"Skill => {row[0]}", end=" ")

        print(f"Progress => {row[1]}%")
    commit_and_close()

def Add_skill():

    sk = input("Enter Skills Name : ").strip().capitalize()

    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uid}'")

    result = cr.fetchone()
    
    if result == None :
        prog = input("Enter Skill Progress : ").strip()

        cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")
    else :
        print("Already Exists")
    commit_and_close()

def Delete_skill():

    sk = input("Write Skill Name: ").strip().capitalize()

    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")

    commit_and_close()

def Update_skill():

    sk = input("Enter Skill Name : ").strip().capitalize()
    prog = input("Enter The NEw Skill Progress : ").strip()
    cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uid}'")
    commit_and_close()

# Check if command exist

if user_input in cmd_list :

    if user_input == "s":

        Show_skills()

    elif user_input == "a" :

        Add_skill()

    elif user_input == "d" :

        Delete_skill()

    elif user_input == "u" :

        Update_skill()

    else:
        print("App Closed")
        commit_and_close()

else:

    print(f"Sorry Command '{user_input}' Not Found")
