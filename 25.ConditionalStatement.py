print("Conditional Statements:")
print("------------------------------")
print("Simple If")
a = 10
b = 20
print("a=", a)
print("b=", b)
if b > a:
    print("B is greater than A")

print("\n")

print("if else")
print("----------")
print("a=", a)
print("b=", b)
if a > b:
    print("A is greater than B")
else:
    print("B is greater than A")

print("\n")

print("If Elif Else")
print("---------------")
a = 20
b = 30
c = 10
print("a=", a)
print("b=", b)
print("c=", c)
if a > b:
    print("A is greater than B")
elif b > c:
    print("B is greater than C")
else:
    print("B is greatest of 3 numbers")

print("\n")

print("Short hand if")
print("-----------------")
print("a=", a)
print("b=", b)
if b > a:
    print("B is greater than A")

print("\n")

print("Short hand if else")
print("----------------------")
print("a=", a)
print("b=", b)
print("A is greater than B") if a > b else print("B is greater than A")

print("\n")

print("Short hand multiples if conditions")
print("-------------------------------------------")
print("a=", a)
print("b=", b)
print("c=", c)
print("A is greater than B") if a > b else print(
    "B is greater than C") if b > c else print("B is greater of 3 numbers")

print("\n")

print("Nested IF")
print("-----------")
print("a=", a)
print("b=", b)
print("c=", c)
if b > c:
    if b > a:
        print("B is biggest number")
    else:
        print("A is biggest number")
else:
    print("C is biggest number")

print("\n")

print("If Elif Else and logic")
print("----------------------")
a = 20
b = 30
c = 10
print("a=", a)
print("b=", b)
print("c=", c)
if a > b and a > c:
    print("A is greater than all numbers")
elif b > c:
    print("B is greater than all numbers")
else:
    print("c is greatest of 3 numbers")

print("\n")

print("If OR")
print("---------------")
a = 20
print("a=", a)
if a == 10 or a == 20:
    print("A is valid")

print("\n")

print("If Not")
print("---------------")
a = 20
print("a=", a)
if not(a):
    print("A is invalid")

print("\n")

print("empty if")
print("---------------")
a = 20
print("a=", a)
if a:
    pass
print("passed")

# no switch conditional statement in python
