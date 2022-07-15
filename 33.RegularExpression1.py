import re
print("Regular Expressions / RegEX")
print("-------------------------------------")
txt = "Hello my name is arniv, ARNIV my contact number is 9090987878."
print(txt)
x = re.search("\AHe", txt)
if x:
    print("Yes string strats with the search pattern.:He")
else:
    print("No string not start with search pattern:He")

print("\n")

# metacharacters
print("RegEx Metacharacters: 11")
print("------------------------")
# meta characters are characters with special meaning
print(txt)
x = re.findall("[a]", txt)
print("Set Charcter []:", x)
x = re.findall("\d\d\d\d\d\d\d\d\d\d", txt)
print("Special Sequence Character \:", x)
x = re.findall("ar..v", txt)
print("Number of any characters patteren . for one, .. for two etc:", x)
x = re.findall("con.*t", txt)
print("Number of 0 or more characters :", x)
x = re.findall("y.+", txt)
print("Number of 1 or more characters after y:", x)
x = re.findall("x.?", txt)
print("Number of 0 or 1 characters after y: ", x)
x = re.findall("x.{3}", txt)
print("Match exact count: ", x)
x = re.findall("^He", txt)
print("starts with He?: ", x)
x = re.findall("78.$", txt)
print("Ends with 78.? :", x)
x = re.findall("arniv|manthew", txt)
print("Either or arniv or mathew in text? :", x)
x=re.search(r"(\b[A-Z]+\b).*(\b\d+)",txt)
print("Groups :",x.groups())
print("Group 0:",x.group(0))
print("Group 1:",x.group(1))
print("Group 2:",x.group(2))
print("Groups 1 and 2 :",x.group(1,2))
print("Group:",x.group())
name,number=x.groups()
#splitting groups values to variables.
print("Name=",name)
print("Number=",number)

print("\n")

# sets
print("Sets")
print("---------")
print(txt)
x = re.findall("[arn]", txt)
print("is text contain a or r or n ? find all :", x)
x = re.findall("[a-d]", txt)
print("is text contain letters between a to d ? find all :", x)
x = re.findall("[0-9]", txt)
print("is text contain any digits from 0 to 9 :", x)
x = re.findall("[a-zA-Z]", txt)
print("is text contain any alphabets small or big ?: ", x)
x = re.findall("[0-3][0-9]", txt)
print(" is text contain value from 00 to 39?", x)
x = re.findall("[^arn]", txt)
print(" list all except a or r or n in text : ", x)
x = re.findall("[+]", txt)
# +, *, ., |, (), $,{} has no special meaning in sets
print("is + in text? : ", x)

print("\n")

# special sequence
print("special sequence:10")
print("--------------------")
print(txt)
x = re.findall("\d", txt)
print("list digits in text: ", x)
x = re.findall(r"\bnum", txt)  # r for raw string
print(" is any word start with num in text: ", x)
x = re.findall(r"er\b", txt)
print(" is any word ends with er in text : ", x)
x = re.findall("78.\Z", txt)
print(" does it end with 98. : ", x)
x = re.findall("\D", txt)
print("find all characters except digits:", x)
x = re.findall("\s", txt)
print("find all space characters : ", x)
x = re.findall("\S", txt)
print("find all characters except space : ", x)
x = re.findall("\w", txt)
print("find all character set a-z or A-Z or 0-9 or _ :", x)
x = re.findall("\W", txt)
print("find all characters other than word characters :", x)
x = re.search("\AHe", txt)
print("string strats with the search pattern.:He ? :", x)

print("\n")

# RegEx functions
print("RegEx Functions:4")
print("------------------")
print(txt)
x = re.search("^Hello.*78\.$", txt)  #for metacharacters to use in pattern use \ escape character before it.
# if no match None will return, multi match only first one returned
print("1.match object returned with search function:", x)
x = re.findall("^Hello.*78.$", txt)
# if no match empty list will return, all matched returns
print("2.list returned with findall function:", x)
x = re.split("\s", txt)
print(" split into list items with space : ", x)
x = re.split("\s", txt, 2)
print(" split into exactly 2 list items :", x)
x = re.sub("\s", "9", txt)
print(" replace all spaces with 9 in text:", x)
x = re.sub("\s", "9", txt, 2)
print(" replace only 2 spaces with 9 : ", x)

print("\n")

# search function methods for retrieving information about the search.
print("search functions properties and methods:")
print("----------------------------------------")
txt = "The Rain Is In Spain."
print(txt)
x = re.search("\s", txt)
print("Start and end position of first occurance of space :",
      x.span())  # returns tuple
x = re.search(r"\bS\w+", txt)
print("Start position of matched pattern first occarnce: ", x.start())
x = re.search(r"\bS\w+", txt)
print(" what string we passed into search pattern function:", x.string)
x = re.search(r"\bS\w+", txt)
print(" display matched string only :", x.group())

print("\n")
