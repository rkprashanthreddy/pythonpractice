# Collections are arrays: 4 built in datatypes
# list: orderered, changeable, dubplicates allowed.
# tuple: ordered, unchangeable, dubplicates allowed.
# sets: unordered, unchangeable, dubplicates not allowed.
# dictionary: ordered( 3.6 to before unordered ), changeable, dubplicates not allowed.

# ordered: when we print they print same order values stored every time, set is unordered
# changeable: we can change, add or remove values from the collection after they created
# dubplicates: dubplicates can be allowed for some because they have ordered index start from
#                    0 is the first index.

# LISTS
print("Lists")
print("------------------------------------------")
# simple string list
fruits = ["apple", "banana", "orange",
          "pineapple", "cherry", "jackfruit", "guava"]
print("simple strings:", fruits)
# simple numeric list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("simple numerics:", numbers)
# simple booelan list
booleans = [True, False, True, True]
print("simple booleans:", booleans)
# simple mixed datatypes
mixedDataTypes = ["Prashanth", 27, True]
print("Mixed Data Types: ", mixedDataTypes)
# dublicate values
dublicates = ["Hello", "Hi", "Prashanth", "Hi", "How", "Hello"]
print("Dubplicates: ", dublicates)
# Multi list multi dimenstional array
multiList = [["Prashanth", "Sana", "Mani"], [1, 2, 3]]
print("Multi List: ", multiList)

print("\n")

# List Functions
print("List Functions")
print("------------------")
cars = ["BMW", "Benz", "Lamborguinni"]
print(cars)
print("Length: ", len(cars))
print("Type : ", type(cars))
thislist = list(("Prashanth", 27, "Banglore"))
print("List Constructor: ", thislist)

print("\n")

# Access Items Inside List
print("List Items Access")
print("---------------------")
students = ["Prashanth", "sana", "mani", "sangeetha", "Naina", "Latha"]
print(students)
print("First Student: ", students[0])
print("Last Student: ", students[-1])
print("Students Except Firs and Last: ", students[1:5])  # range of indexes
print("Second last 2 students: ", students[-3:-1])
print("Any Student: ", students[3])
print("Start to middle students: ", students[:3])
print("Middle to last students: ", students[3:])

print("\n")

# Change List Items
print("Modify List Items")
print("----------------------")
flowers = ["lilly", "lotus", "rose", "jasmine"]
print(flowers)
flowers[1] = "sunflower"
print("Changing lotus to sunflower: ", flowers)
flowers[1:3] = ["tulip", "marigold"]
print("Chaning 2nd and 3rd flower name: ", flowers)  # range of indexes
flowers[1:3] = ["hibiscus", "lavender", "daffodil"]
print("More values passing than range of index: ", flowers)  # size of list grows
flowers[1:2] = ["Geranium", "Poppy"]
print("Multiple insertions at one index: ", flowers)
print(flowers)
# flowers[0:2] = "Royal Orchid" # if we given without [ ] for ranged assignment, royal orchid every letter is stored
# as single item in the list like ["R","o","y","a","l","O","r","c","h","i","d",rest of the list]
flowers[0:2] = ["Royal Orchid"]
print("Multiple Indexes Passed only single values: ",
      flowers)  # size of list shrinks

print("\n")

# Add new items to the list
print("Add Items to the List")
print("---------------------------")
animals = ["cat", "dog", "rabbit", "lion"]
print(animals)
# print("Append last to animals with Tiger: ", animals.append("Tiger")) #result will be none, first only append and print
animals.append("Tiger")
print("Append last to animals with Tiger: ", animals)
animals.insert(2, "Rat")
print("Insert rat at index 2 in animals: ", animals)
moreAnimals = ["cow", "elephant", "ant"]
print(moreAnimals)
animals.extend(moreAnimals)
print("Combine animals and more animals: ", animals)
birds = ("crow", "pegion", "love birds")
print(birds)
animals.extend(birds)
print("Combine list and iterable object tuple: ", animals)
# it can extend tubple, set, dictionaries, if dictionaries extended only keys will be taken.
student = {"Name": "Prashanth", 27: "Age"}
print(student)
animals.extend(student)
print("if list extend dictionary: ", animals)
# 2 lists cant be extended. only one can be extended at a time

print("\n")

# remove list items or delete list
print("Remove List Items Or Delete List")
print("------------------------------------------")
tens = [10, 20, 30, 40, 50]
print(tens)
tens.remove(20)
print("Remove 2o: ", tens)
# print("Remove 2nd index item: ", tens.pop(2)) # givs wrong result
tens.pop(2)
print("Remove 2nd index item: ", tens)
tens.pop()
print("Remove Last item: ", tens)
del tens[0]
print("Delete 0th Index: ", tens)
del tens
# print("Delete the list:" tens)    # gives error as it is deleted
tens = [10, 20, 30, 40, 50]
tens.clear()
print("Clear all the items from list: ", tens)

print("\n")

# loop lists
print("Loop Lists")
print("-------------")
banks = ["CBI", "CAN", "SBI", "AXIS", "DCB"]
print(banks)
print("Looping through every item:")
for x in banks:
    print(x)
print("Looping through indexes:")
for i in range(len(banks)):
    print(banks[i])
print("Looping through while loop:")
i = 0
while i < len(banks):
    print(banks[i])
    i += 1
print("Loop like do while, do while loop does not exhist in python: ")
i = 0
while True:
    print(banks[i])
    i = i+1
    if(i >= len(banks)):
        break
print("Loop with shorthand for loop called as list comprehension")
[print(x) for x in banks]
print("newlist  only bank names that have 'I' in them:")
newlist = []
for x in banks:
    if "I" in x:
        newlist.append(x)
print(newlist)
print("\n")

# List comprehension
print("List Comprehension")
print("-------------------------")
fruits = ["mango", "apple", "orange", "banana", "cherry", "kiwi"]
print(fruits)
newlist = [x for x in fruits if "a" in x]
print("New List with only fruits have \"a\" in them: ", newlist)
newlist = [x for x in fruits]
print("New List with all the fruits from fruits list: ", newlist)
newlist = [x for x in fruits if x != "apple"]
print("New List without \"apple\" :", newlist)  # condition acts as a filter
newlist = [x for x in range(10)]
print("New List with range of 10: ", newlist)
# it can be any iterable object like list, tuple, set etc
newlist = [x for x in range(10) if x < 5]
print("New List with range 10 only numbers under 5: ", newlist)
# manupulate data before it place into list
newlist = [x.upper() for x in fruits]
print("New List From fruits to upper cased all name: ", newlist)
newlist = ['hello' for x in fruits]
print("Set new list to whatever data number of items equal to fruits list: ", newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print("except banana  copy to list, if banana found then change to orange: ", newlist)
# it copies items from fruits lsit to new list comparing all the items , if item is banana then
# it is not copied if item found banana then changes to orange and copies.

print("\n")

# Sort Lists
print("List sort")
print("-----------")
brands = ["Adidas", "Nike", "John Players", "Fila"]
prices = [200.30, 100.00, 9999.99, 398.99]
print(brands)
print(prices)
brands.sort()
print("Sort brands ascending: ", brands)
brands.sort(reverse=True)
print("Sort brands decending: ", brands)
brands.reverse()
print("Sort brands revers:", brands)
prices.sort()
print("sort prices low to high: ", prices)
prices.sort(reverse=True)  # keyword argument
print("sort prices high to low: ", prices)


def sorter(n):
    return abs(n-50)


prices.sort(key=sorter)
print("sort prices near to 50 first: ", prices)  # key function
brands = ["Adidas", "nike", "John Players", "fila"]
print("New brands:", brands)
brands.sort()
print("sort case sensitive default:", brands)
brands.sort(key=str.lower)  # inbuilt function as key
print("sort case insensitive: ", brands)

print("\n")

# List copy :copy(), list()
print("List Copy")
print("------------")
thislist = ["Hello", "Hi", "How"]
newlist = thislist.copy()
print(newlist)
newlist2 = list(thislist)
print(newlist2)
# if list2=list1 then changes in list1 also affects items in list2, becuase its reference to list 1
list1 = [1, 3, 4, 5]
list2 = list1
print("list1:", list1)
print("list2:", list2)
list1.append(40)
print("list1:", list1)
print("list2:", list2)
# wont work change if list3=list1+list2 like this two lists into 1 list will not affect items even
# after they change in main list1 or list2, list3 remains same as before change.

print("\n")

# Joins
print("Joins or concatination of lists 2 or more")
print("--------------------------------------------------")
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print("list1=", list1)
print("list2=", list2)
list3 = list1+list2
print("list3 join of list1 and list2=", list3)
print("direct print of list1 and list2 join:", list1+list2)
print("join or add with loop.")
for x in list2:
    list1.append(x)
print(list1)
list1.extend(list2)
print("list1 extends list2:", list1)

print("\n")

# list methods
'''
1. append()
2.copy()
3. insert()
4.sort()
5.reverse()
6.extend()
7.remove()
8.pop()
9.clear()
10.index()
11.count()
'''
print("List Methods")
print("----------------")
list1 = [1, 2, 0, 1, 2, 3, 4, 2, 1]
print(list1)
print("count of 1's in list1: ", list1.count(1))
# return index of first occurance.
print("index of 2 in list1: ", list1.index(2))
