print("Dictionary")
print("-------------")
student = {"Name": "Anvir", "Age": 20}
print("Simple Dictionary=", student)
numberkeys = {10: "Ten",
              20: "Twenty",
              30: 40}
print("Numeric keys dictionary=", numberkeys)
car = {
    "brand": "ford",
    "origin": "USA",
    1998: "year",
    "still there": True,
    "branches": ["Banglore", "Delhi", "Mumbai"]
}
print("Multi datatyped dictionary=", car)
emptydict = {}
print("Empty Dictionary:", emptydict)
students = {
    "student1": {
        "Name": "Naveen",
        "Age": 20
    },
    "Student2": {
        "Name": "Siddarth",
        "Age": 23
    }
}
print("Nested Dictionary=", students)
car1 = {
    "Name": "Lamborguinni",
    "Country": "USA"
}
car2 = {
    "Name": "Tata",
    "Country": "India"
}
cars = {
    "car1": car1,
    "car2": car2
}
print("mutliple dictionaries to one dictionary=", cars)
celebrities = {
    "Name": "Sonu Nigham",
    "Desig": "Singer",
    "Desig": "Hinustani Singer"
}
print("dublicates are not allowed, if dubplicates values replaced=", celebrities)

print("\n")

# Dictionary functions
print("Dictionary Functions:")
print("----------------------")
capitals = {
    "India": "New Delhi",
    "USA": "Washington DC",
    "China": "Beijing",
    "Canada": "Toronto",
    "UK": "London",
    "Russia": "Moscow"
}
print(capitals)
print("Number of items:", len(capitals))
print("Type check:", type(capitals))
y = dict(Name="Prashanth", Age=27)
print("Dictonary Constructor:", y)

print("\n")

# adding items or changing items
print("Adding items or changing items")
print("------------------------------")
print("1.With Keys")
print(capitals)
print("Adding Brazil:")
capitals["Brazil"] = "Tel Aviv"  # adding new key value
print(capitals)
# changing value by key, if that key is not there then it will be added new item
print("Changing Russian Capital Name:")
capitals["Russia"] = "Great Moscow"
print(capitals)
print("2.With update() function ")
print("Adding Singapore:")
# adding as item, update must be dictionary or iterable object with key value pairs
capitals.update({"Singapore": "Singapore City"})  # argument given to update
print(capitals)
print("Updating UK Capital:")
# changing value, if key not exist then it will be added new item
capitals.update({"UK": "London City"})
print(capitals)

print("\n")

# accessing items of dictionary
print("Items Access:")
print("----------------")
# value associated with key is getted
print("Item from capitals with key:", capitals["Canada"])
print("Item from capitals with get method:", capitals.get("Canada"))
print("Print all keys of capitals dict:", capitals.keys())
print("Print all values from capitals dict:", capitals.values())
print("Print all items from dict:", capitals.items())
if "New Delhi" in capitals.values():
    print("Yes")
x = capitals["USA"]
print("X=", x)
print("accessing from nested dictionary:", students["student1"]["Name"])
print("\n")

# removing items from dictionary
print("Items remove from dictionary")
print("----------------------------")
print("1.pop")
print(capitals)
capitals.pop("USA")
print("After Removing USA:", capitals)
print("2.popitem")
capitals.popitem()
print("Last item is removed:", capitals)
print("3.del key")
del capitals["Canada"]
print(" deleted Canada:", capitals)
print("4. remove all items dictionary")
capitals.clear()
print(capitals)
print("5.delete dictionary: use del")
del capitals
# print(capitals)  # gives error as its deleted

print("\n")

# Loop dictionaries
print("loop dictionaries")
print("-----------------")
borders = {
    "India": "Nepal,Butan,China,Pakistan,Afghanisthan,Bangladesh,Myanmar",
    "USA": ["Canada", "Mexico"],
    "Saudi Arabia": ("Omen", "Yemen", "UAE", "israil", "egypt"),
    "Bhutan": {"China", "India"}
}
print("for in loop:")  # default gives keys only
print("only keys method 1")
for x in borders:
    print("\t", x)
print("only keys method 2")
for x in borders.keys():
    print("\t", x)
print("only values method 1")
for x in borders.values():  # only gives values
    print("\t", x)
print("only values method 2")
for x in borders:  # only gives values
    print("\t", borders[x])
print("items as 2 variables")
for a, b in borders.items():  # items and keys both
    print("\t", a, ":", b)
print("items as single variable")
for a in borders.items():  # items as it is
    print("\t", a)
print("Final a will be last item from last run loop")
print("\t", a)

print("\n")

# copy dictionaries
print("copy dictionaries: use copy() or dict()")
print("--------------------------------------- ")
dict1 = {10: 20, 100: 200, 1000: 2000}
dict2 = dict1.copy()
print("Dict1:", dict1)
print("Dict2:", dict2)
dict3 = dict(dict2)
print("Dict2:", dict3)

print("\n")

# dictionary methods
print("Dictionary Methods:")
print("--------------------")
'''
1.get()
2.items()
3.values()
4.items()
5.update()
6.clear()
7.copy()
8.pop()
9.popitem()

'''
print("fromkeys()")
x = ("a", "b", "c", "d")
y = 20
print("create dictionary with tuple x as keys")
# from specified keys specified value for all keys.
thisd = dict.fromkeys(x, y)
print(thisd)
# only keys passed then values will be None its default value.
thisd2 = dict.fromkeys(x)
print(thisd2)
for x in dict.fromkeys(x, y):
    print(x)
print("setdefault()")
# use key and value, if value associated with key in the dictionary it will print that value.
# if that key and value not in dictionary then it will insert that new key and value into dictionary.
x = {1: 1, 2: 2, 3: 3}
print(x)
y = x.setdefault(3, 4)  # 3 is there so 3s value prints
print(y)
y = x.setdefault(4, 4)  # 4 is not there so adds 4 into x and prints 4s value
print(y)
print(x)  # new x after add by setdefault

print("\n")

# taking input value from user and adding to dictionary keys
student = {
    "Full Name": None,
    "Age": None
}
print(student)
fullName = input("Enter Student Full Name:")
age = int(input("Enter Students Age:"))
student.update({"Full Name": fullName})
student["Age"] = age
print(student)
