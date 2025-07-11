list1 = [1, 2, 3, 4, 5,]
list2 = ["A", "B", "C"]
tuple1= ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name": "Osama", "Age": 36, "Country": "DZ"}

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):
    print("List 1 Item => ", item1)
    print("List 2 Item => ", item2)
    print("Tuple 1 Item => ", item3)
    print("Dict 1 Key =>", item4, "Value => ", dict1[item4])
