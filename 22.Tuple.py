print("Tuple")
print("-----------------------")
fruits = ("mango", "orange", "kiwi")
print("Normal Tuple:", fruits)
ages = (10, 20, 30, 40, 50)
print("different data type tuple:", ages)
bools = (True, False, True, False)
print("boolean tuples:", bools)
mixed = ("Hello", 2, True)
print("Mixed tuple:", mixed)
singles = ("his",)
print("Single item tuple:", singles)
dublicates = ("hello", "hi", "prashanth", "prashanth", "hi")
print("Dubplicates in tuple:", dublicates)

print("\n")

# tuple functions
print("tuple functions")
print("---------------------")
googles = ("sunglasses", "zero power", "powered", "bluelight filter")
print(googles)
print("Length of tuple:", len(googles))
print("Type check:", type(googles))
tup = tuple(("hi", "how", "are", "you"))
print("tuple constructor:", tup)

print("\n")

# access tuples
print("Tuple items access")
print("------------------------")
devices = ("TV", "Laptop", "PC", "SmartPhone", "Ipod", "Tablet")
print(devices)
print("First device:", devices[1])
print("Last device:", devices[-1])
print("Devices except first and last:", devices[1:5])
print("Devices from start to middle:", devices[:3])
print("Devices from middle to last:", devices[3:])
print("Devices from last second to last 4:", devices[-4:-1])

print("\n")

# Change or add or remove or delete or update tuple
print("Tuple modification: since its unchangeable we cant, but other ways we can")
cloths = ("pant", "shirt", "gown", "saree", "t-shirt", "trousers")
print(cloths)
print("Change Tuple Pant to Pants, change to list do changes and convert back to tuple")
y = list(cloths)
print("List y", y)
y[0] = "pants"
print("List y after change:", y)
cloths = tuple(y)
print("Tuple after change:", cloths)
print("Adding item to tuple: 1. can do as convert tuple to list, add and convert to tuple")
print(cloths)
y = list(cloths)
y.append("jeens")
cloths = tuple(y)
print("cloths after append:", cloths)
print("2.adding other tuple")
print(cloths)
cloths2 = ("jerkin", "hoodie")
cloths += cloths2
print("Cloths now:", cloths)
print("Removing item: covert to list, remove , convert back to tuple")
print(cloths)
y = list(cloths)
y.remove("hoodie")
cloths = tuple(y)
print("Hoodie removed tuple:", cloths)
print("deleting entire tuple: use del ")
del cloths
# print("cloths") through error as its deleted

print("\n")

# unpack tuples
print("unpack tuples")
print("equal number of variables as number of items in tuple:")
browsers = ("google", "bing", "safari", "edge", "opera", "onion", "firefox")
print(browsers)
a, b, c, d, e, f, g = browsers
print("a=", a)
print("b=", b)
print("c=", c)
print("d=", d)
print("e=", e)
print("f=", f)
print("g=", g)
print(browsers)
print("if unequal variables then error arises:")
# a,b=browsers
print("use of * for last variable:")
x, y, *z = browsers
print("x=", x)  # first item
print("y=", y)  # second item
print("z=", z)  # remaining items as list
print("use of * to middle variables")
x, *y, z = browsers
print("x=", x)  # first item
print("y=", y)  # middle items remaining
print("z=", z)  # last item
print("other case with 4 variables:")
x, *y, z, a = browsers
print("x=", x)  # first item
print("y=", y)  # middle items remaining
print("z=", z)  # last second item
print("a=", a)  # last item

print("\n")

# loop tuples
print("tuple loops")
print("----------------------")
print(browsers)
print("for loop through items:")
for x in browsers:
    print(x)
print("for loop through indexes:")
for i in range(len(browsers)):
    print(browsers[i])
print("while loop")
i = 0
while i < len(browsers):
    print(browsers[i])
    i += 1
print("do while loop style")
i = 0
while True:
    print(browsers[i])
    i += 1
    if(i >= len(browsers)):
        break

print("\n")

# join tuples
print("Join tuples")
print("---------------------------")
print("join with +")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("tuple1:", tuple1)
print("tuple2:", tuple2)
tuple3 = tuple1+tuple2
print("tuple3=", tuple3)
print("join with multiplication")
print(tuple1)
print("tuple1 multiplied by 2:", tuple1*2)
print("tuple1 multiplied by 5:", tuple1*5)

print("\n")

# tuple methods
print("tuple methods:")
print("-------------------")
x = (1, 3, 4, 5, 6, 7, 8, 9, 1, 2, 1, 2, 1)
print("Index of first 1 in x:", x.index(1))
print("Number of 1's in x:", x.count(1))
