print("sets")
print("---------------")
alphabets = {"a", "b", "c", "d", "e", "f", "g", "h"}
print("Normal set:", alphabets)
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print("Numeric set:", numbers)
booleans = {True, False, True, True}  # repeated items not stored and excluded
print("Booleans set:", booleans)
mixed = {"Prashanth", 27, True}
print("Mixed set:", mixed)
print("second time print mixed set:", mixed)
# un ordered every time print order changes
print("third time print mixed set:", mixed)
dublicates = {'hi', 'hello', 'hi'}
print(dublicates)   # dublicates excluded as sets cant contain dubplicates

print("\n")

# set functions
print("set functions")
print("-----------------")
print(alphabets)
print("Length of set:", len(alphabets))
print("Type check:", type(alphabets))
y = set(("hi", "hello", "how"))
print("Set constructor:", y)

print("\n")

# access set items
print("set items access:")
print("-----------------------")
print("no indexed set so only by for loop or in operator we can access or check")
print(alphabets)
print("using for loop:")
for x in alphabets:
    print(x)
print("check with in operator")
if "a" in alphabets:
    print("is there")
else:
    print(" a is not there")

print("\n")

# add item
print("add item:")
print("--------------")
print("using add method")
print(alphabets)
# alphabets.add("i", "j")  # error arise as we can only add one one item with add method.
alphabets.add("i")
print(alphabets)
print("using update method add other set")
print(alphabets)
print(numbers)
alphabets.update(numbers)
print(alphabets)
print("add any iterable")
x = ("prashanth", "banglore")
print(x)
alphabets.update(x)
print(alphabets)

print("\n")

# remove items from set
print("remove items from set")
print("---------------------------------")
print(" 1. using remove method")
print(alphabets)
alphabets.remove("banglore")  # if banglore is not in set then error will occur
print(alphabets)
print("2. using discard method")
print(alphabets)
# if item not in list then no error occur set print same
alphabets.discard("prash")
print("delete item not in set, print same set:", alphabets)
alphabets.discard("prashanth")
print("delete item:", alphabets)
print("3.clear method to empty set")
print(alphabets)
alphabets.clear()
print(alphabets)
print("4, using del key word delete full set:")
del alphabets
# print(alphabets) # gives error as its not existed
print("5. using pop to remove last element, but not sure what will delete as its unorderd")
print(numbers)
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)

print("\n")

# loop sets
print("loop sets")
print("-------------")
print("for loop only")
print(numbers)
for x in numbers:
    print(x)
# we cant use while loop as sets not the indexed

print("\n")

# join sets
print("Sets join : union new set style, update no new set creation style")
print("---------------------")
print("1. union join")
x = {1, 2, 3, 4, 5}
y = {6, 7, 8, 9, 10}
print(x)
print(y)
z = x.union(y)              # all join , same for update also
print(z)
print("2.intersection")  # only dublicates select, same for update also
x = {1, 2, 3, 4, 5}
y = {6, 7, 8, 9, 1}
print(x)
print(y)
z = x.intersection(y)
print(z)
# except dublicates all items select, same for update also
print("3.symmetric_difference")
x = {1, 2, 3, 4, 5}
y = {6, 7, 8, 9, 1}
print(x)
print(y)
z = x.symmetric_difference(y)
print(z)
print("4.update")
x = {1, 2, 3, 4, 5}
y = {6, 7, 8, 9, 1}
print(x)
print(y)
x.update(y)
print(x)
print(y)
print("4.intersection_update")
x = {1, 2, 3, 4, 5}
y = {6, 7, 8, 9, 1}
print(x)
print(y)
x.intersection_update(y)
print(x)
print(y)
print("4.symmetric_differance_update")
x = {1, 2, 3, 4, 5}
y = {6, 7, 8, 9, 1}
print(x)
print(y)
x.symmetric_difference_update(y)
print(x)
print(y)

print("\n")

# set copy
print("set copy")
print("------------------")
names = {"prashanth", "sana"}
print("names set:", names)
x = names.copy()
print("copied set x:", x)

print("\n")

# set methods
print("set methods: 17")
print("-------------------------")
'''
1. add()
2. pop()
3. remove()
4. clear()
5. update()
6. union()
7. intersection()
8. symmetric_difference()
9. intersection_update()
10. symmetric_difference_update()
11. discard()
12. copy()
13. differance()
14.differance_update()
15. isdisjoint()
16. issubset()
17. issuperset()
'''
print(" difference : new set contain items from set 1 and 2 ")
print("                    items only exist in set 1 and not in set 2")
x = {1, 2, 3, 4, 5}
y = {1, 3, 4, 10}
print(x)
print(y)
z = x.difference(y)
print(z)
print(" difference_update : set update contain items from set 1 and 2 ")
print("                                 items only exist in set 1 and not in set 2")
x = {1, 2, 3, 4, 5}
y = {1, 3, 4, 10}
print(x)
print(y)
x.difference_update(y)
print(x)
print(y)
# if we use here or in before of any methods like z=x.differance_update(y) for updates style
# print(z) will be none value contained, as its not create new set only updates.
print(" isdisjoint: set 1 and set 2 items not similar then return True ")
x = {1, 2, 3, 4, 5}
y = {9, 8, 7, 10}
print(x)
print(y)
# we need to store return value in some variable or can directly use in print
z = x.isdisjoint(y)
print(z)
print(" issubset : set 1 contain any items from set 2? ")
x = {1, 2, 3}
y = {1, 3, 4, 10, 2, 7, 8}
print(x)
print(y)
z = x.issubset(y)
print(z)
print(" issuperset : set 2 is super set of set 1?")
x = {1, 2, 3, 4, 5}
y = {1, 3, 4, 10, 2, 7, 8}
print(x)
print(y)
z = x.issuperset(y)
print(z)
