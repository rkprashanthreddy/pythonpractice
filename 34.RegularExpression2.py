print("Regular Expression 2")
print("---------------------------")
import re
text="""Hello my name is arniv, my contact numbers are +91 4398298398, 3458783989 and my 
             residence number is 2345-894893. My personal mail is arniv@gmail.com, my official
             mail is Arniv_34@mans.co.in. My joined date is 12-Jun-2022, my birthdate is 10/12/2001.
             I have sheduled on 21.09.2021. 
        """
print(text)
#dates extracting from text
datePatteren=re.compile("\d{2}[./-]([a-zA-Z]{3}|\d{2})[./-]\d{2}")
print("With Search function only first occurance of details match.")
print("-----------------------------------------------------------")
matches=datePatteren.search(text)
print(matches)

print("\n")

print("With finditer function we can loop through all the match objects.")
print("-----------------------------------------------------------------")
matches=datePatteren.finditer(text)
for match in matches:
    print(match)

print("\n")

print("With finditer function we can loop through all the matches.")
print("-----------------------------------------------------------")
matches=datePatteren.finditer(text)
for match in matches:
    print(match.group())

print("\n")

print(text)

#dates extracting from text
print("Dates:")
print("------")
matches=datePatteren.finditer(text)
for match in matches:
    print(match.group())

print("\n")

#emails extracting from text
print("Emails:")
print("-------")
emailPatteren=re.compile("\w+@[a-z]+(\.[a-z]{2,3})+")
matches=emailPatteren.finditer(text)
for match in matches:
    print(match.group())

print("\n")
#phone numbers extracting from text
print("Phone Numbers:")
print("--------------")
phonePatteren=re.compile(r"(\+\d{2,3}|\d{4})?[\s-]?\d{6,10}")  #used here as raw string means \n etc also included.
matches=phonePatteren.finditer(text)
for match in matches:
    print(match.group())

print("\n")

#grouping 2
print("Grouping 2")
print("----------")
txt="Hello arniv, costs of gruits as follows: APPLE 200 ruppes, BANANA 50 rupees, PINEAPPLE 70 rupees."
print(txt)
print("\n")
x=re.compile(r"(\b[A-Z]+\b).(\b\d+\b)")
for match in x.finditer(txt):
    print(match.group())
    print(match.group(1,2))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())
    print("\n")
for match in x.finditer(txt):
    print(match.group())

print("\n")

#grouping 3
print("Grouping 3")
print("----------")
students='''
            Name=Mani
            Class=10th
            Score=99%

            Name=Sita
            Class=10th
            Score=100%

            Name=Smitha
            Class=9th
            Score=98%
        '''
print(students)
print("\n")
#patteren=re.compile("Name=([a-zA-z]+)\n")  #either way works
patteren=re.compile("Name=(\w+)\n")
print("Student Names:")
print(patteren.findall(students))

print("\n")

#hide sensitive information or data
information="Arniv's salary was $89,3909 in 2019 but its grew upto $100,9999 in 2020"
print("Without Hidden Data: ",information)
print("Way 1:")
x=re.sub("\$[0-9,]+","**********",information)
print("With Hidden Data: ",x)
print("Way 2:")
patteren=re.compile("\$[0-9,]+")   # using compile function of re its faster less redundency
matches=patteren.sub("*****",information)
print(matches)