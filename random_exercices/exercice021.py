import pandas
file_txt = input("Enter The File Name Without Extension : ").strip()
delm_input = input("Enter The Delimiter You Have Used In Your File : ").strip()
my_data = pandas.read_csv(f"{file_txt}.txt", delimiter=delm_input)
my_data.columns = ["Name", "Points"]
my_data.to_csv("points.csv", index=None)
print("Done ✅")
