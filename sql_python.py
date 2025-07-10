import sqlite3

db = sqlite3.connect("test.db")

db.execute("create table if not exists skills (name text,user_id integer)")

my_list = ["Mohamed", "Ahmed", "Mustapha", "Omar"]

for key, user in enumerate(my_list):
    db.execute(f"insert into skills(name, user_id) values({key + 1}, '{user}')")

db.commit()

db.close()
