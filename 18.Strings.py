# Normal String, both " or ' quotes can be used and they mean the same
print("Normal String")
x = "Hello Prashanth "
y = 'Hello Prashanth'
print(x, y)

print("\n")

# Multi line String, 3 """ or ''' quotes can be used and they mean the same
print("Multi Line String")
x = """ Hello Prashanth
how are you how do you do
        i am fine thank you"""
y = '''Hello Prashanth
how are you how do you do
i am fine thank you.'''
print(x)
print(y)

print("\n")

# strings are arrays, we can loop, get indexed unicode character.
print("String is array of unicode characters")
txt = "Hello Prashanth"
print(txt, " ", txt[1])

print("\n")

# string length
print("string length", len(txt))

print("\n")

# check presence of sub string in string
print("Check the substring presence")
print("Prashanth" in txt)   # true if present, false if not
if ("Hello" in txt):
    print("Yes is there")
print("Mani" not in txt)   # true if not present, false if present
if("Mani" not in txt):
    print("Not Present")

print("\n")

# looping through the string since it is an array its possible to loop
print("string loop")
for i in txt:
    print(i)

print("\n")

# String Slicing to get sub string or characters between specified start and end indexs
# index starts from o(zero)
print("String Slicing")
print(txt)
print("string slice middle to middle index: ", txt[3:7])
print("string slice from start to middle index: ", txt[:7])
print("string slice from middle to last index: ", txt[3:])
# from last index start from 1, 2 is not included
print("string slice from last index to last index: ", txt[-5:-2])

print("\n")

# String Methods
print("String Methods")
print(txt)
print("upper case: ", txt.upper())
print("lower case: ", txt.lower())
print("first letter capital: ", txt.capitalize())
txt2 = " Hello "
print("outer spcaces remove: before (", txt2, ") after(", txt2.strip(), ")")
txt3 = "Hello, Prashanth"
print("split into list: ", txt3.split(","))
print("replace: ", txt.replace("H", "J"))
print("find: ", txt3.find("P"))
txt4 = "Hello prashanth"
print("check its title style? ", txt4.istitle())
print("make title style: ", txt4.title())
txt5 = txt4.title()
print(txt5.istitle())
print("isdigit: ", txt4.isdigit())
print("isnumeric: ", txt4.isnumeric())
print("isspace: ", txt.isspace())
print("isdecimal: ", txt.isdecimal())
# gives lowercase but same lower() also gives lowercase
print("casefold: ", txt.casefold())
txt6 = "hehelh"
print("count: ", txt6.count("h"))
print("islower: ", txt.islower())
print("isupper: ", txt.isupper())
print("encode: ", txt.encode())
print("startswith: ", txt.startswith("H"))
print("endswith: ", txt.endswith("h"))

print("\n")

# string formatting, by this we can combine string and numerals. where regular + concatination
# dont work when we try to concat string with number.
print("String Formatting")
age = 27
# there should be no space { } it should be {}
txt = " My name is prashanth, i am {} years old."
print(txt.format(age))

# multiple format arguments
txt2 = " My name is {}, i am {} years old. "
print(txt2.format("Prashanth", 27))

# indexed format
txt3 = " My name is {1},i am {0} years old."
print(txt3.format(age, "Prashanth"))

print("\n")

# escape characters ',",backspace,tab,/,hexa,octa, carriage return,newline
print("hello 'world'")
# if we use \ last then we need to add escape character \ to \\ to work
print("slash:escape character: \\")
print("double quots:Hello my name is \"Prashanth\"")
print("backspace:Hello \bWorld")
print("tab:Hello\tWorld")
# some what confusion there need to understand it
print("carriage return:Prashanth\rReddy")
print("new line:Hello \n World")
print("middle slash:hello \ world")      # in middle if we use \ no need \\
print("octal value:\110\145\154\154\157")
print("hex value:\x48\x65\x6c\x6c\x6f")
