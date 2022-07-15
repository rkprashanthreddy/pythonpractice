print("While Loop:")
print("-----------------")
cars = ["porsche", "lamborguinni", "audi", "rolls rover",
        "rolce royce", "volks wagen", "bucati", "bmw"]
print(cars)
i = 0
while i < len(cars):
    print(cars[i])
    i += 1

print("\n")

print("Do while style with break")
print("--------------------------------")
# do while loop does not in python, other technique to work as do while
print(cars)
i = 0
while True:
    print(cars[i])
    i += 1
    if i >= len(cars):
        break

print("\n")

print("For in loop or for loop")
print("----------------------------")
print(cars)
print(" way 1")
for x in cars:
    print(x)
print("way 2")
for i in range(len(cars)):
    print(cars[i])

print("\n")

print("break and continue")
print("-------------------")
i = 0
while i < 6:
    i = i+1
    if i == 3:
        continue
    print(i)
print("\n")
for i in range(6):
    print(i)
    if i == 3:
        break
	
print("\n")

print("Pass in for:")
print("------------")
for i in range(6):
    pass
print("for passed")

print("\n")

print("Else in loops")
print("-------------")
i=0
while i<6:
    print(i)
    i+=1
else:
    print("Loop Success")
print("\n")
for x in range(10):
    print(x)
else:
    print("Done Looping.")

print("\n")

print("Range in for")
print("------------")
print("Range between.")
for i in range(2,10):
    print(i)

print("\n")

print("Range steps jump")
print("----------------")
for i in range(0,10,2):
    print(i)

print("\n")

print("Nested Loops:")
print("-------------")
l1=["red","green","orange"]
l2=['hani','sini','pini']
for x in l1:
    for y in l2:
        print(x,y)
