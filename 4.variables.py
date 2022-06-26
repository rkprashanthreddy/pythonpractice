# No declaration or type specification required, variables are created as soon as values are assigned.
x = 10
print(x)

# Variables can be overwritten datatype accordingly to value
x = 10       # its int
x = "Hello"  # its string
x = 'Hello'  # its also string single or double quotes no matters
print(x)     # outputs Hello

# Error if we dont assign a value to the variable when it is created, cant create empty variable.
# if we run in command prompt error might not show, if we use IDE error arise as x is not defined.
# if we use python interface gives error as soon as we press enter after >>>x, Error: x is not defined.
x
x = 10
print(x)

# variables are case sensitive, the following are two different variables
# A will not overwrite a
a = 10
A = "Hello"
print(A)
print(a)
print(type(A), type(a))

# valid variable names start with _(underscore),alphabets(a-z / A-Z) followed by any _,alphabet or digit
_x = 10
print("_x:", _x)
x2 = 20
print("x2:", x2)

# invalid variables space between variable names, keywords as variable names, variable start with digit or contain any
# other character
# full name="hello" # space inbetween is invalid
# 2afe=20           # digit start is invalid
# print=200         # keyword or reserved word as variable is invalid
# hello$*="hi"      # other characters included as variable is invalid

# variable name writing convenstions
x = 20                         # simple variable
age = 20                       # variable with meaning

# two or more words variable name
fullName = "Prashanth Reddy"   # 1.camel case
FullName = "Prashanth Reddy"   # 2.Pascal case
full_name = "Prashanth Reddy"  # 3.snake case
# 4.general case, pretty much not used for easy reading sake.
fullname = "Prashanth Reddy"

print(fullName, FullName, full_name)

# Multiple variables assigning
x, y, z = 10, 20, 30
print("x,y,z")
print("x:", x)
print("y:", y)
print("z:", z)

# single value to multiple variables
x = y = z = "Prashanth"
print("x=y=z")
print("x:", x)
print("y:", y)
print("z:", z)

# unpack a collection
fruits = ["apple", "banana", "orange"]
x, y, z = fruits
print("x,y,z=fruitsCollection")
print("x:", x)
print("y:", y)
print("z:", z)

# Error too many values to unpack , due to less variables than values in collection.
#fruits = ["apple","banana","orange"]
#a, b = fruits
#print("a:", a)
#print("b:", b)

# maths with variables
x = 10
y = 20
print("x+y=", x+y)

# string+number print gives error
x = 10
y = " years old"
# print(x+y)
# but can resolve with
print(x, y)

# string+string =concatination
x = "10"
y = " years old"
print(x+y)

#global variables
x = 10


def simpleCall():
    print("x inside function:", x)


simpleCall()
print("x outside function:", x)

# global variable override inside function
x = 10


def simples():
    x = 20
    print("x inside function override x global:", x)


simples()
print("x outside function same remains:", x)

# local variable will be inside function only works, or inside perticular block only works
# global variable creation inside the function use global keyword before variable


def globs():
    # global x = "hello" # gives invalid syntax error
    global x
    x = "hellow"
    print("inside function, global variable:", x)


globs()
print("outside function, can also use global variable:", x)

# change global variable inside function with local variable
x = 200
print("before change x:", x)


def sing():
    # global x = 100 #gives invalid syntax error
    global x
    x = 100


# we need to call it to run statements inside function, without call inside statements wont run and x still remain 200
sing()

print("x after change:", x)
