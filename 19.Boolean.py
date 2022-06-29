# Boolean returns only true or false
# regular print
print(10 > 9)
print(9 == 9)

# with if condition checking
a = 10
b = 9
if(a < b):
    print(" a is greater than b")
else:
    print("b is greater than a")

# evaluate values and variables
# use of bool() function()
print(bool("Helo"))
print(bool(27))
print(bool(['hello', 'how']))
x = "Hello"
y = 27
print(bool(x))
print(bool(y))
# false happens below conditions, empty list etc
print(bool(0))
print(bool(False))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(None))
print(bool(""))
# any string is true except if it is empty
# any number is true except if its is 0
# any list,tuple,dictionary,set are true except empty ones.

#functions and booleans
print("\n functions and booleans")


def retFunction():
    return True


print(retFunction())

# condition check with function booleans
if retFunction():
    print("Yes")
else:
    print("No")

# check datatype with isinstance built in function
print("\n isinstance")
x = 200
print(x, isinstance(x, int))


# other bool false case
class myClass:
    def __len__(self):
        return 0


myObject = myClass()  # object assigned to class that return 0
print(bool(myObject))
