#unlike sort() which actully modifies the iterable, sorted() will only display without modifying.

print("Sorted")
print("-------")
print("reverse sorting")
print("---------------")
lister=[1,2,3,4,5]
print(sorted(lister,reverse=True))  #descending order sort numbers.
print(lister)  #will be same as first, actull value is not modifed.

print("\n")
print("different data types sorting")
print("----------------------------")
lister=["a","c","d","h","g"]
tupler=(20,5,8,70,3)
#mixedLister=[1,"b","c","z",10,20,0,"m",9,True]   #str and int cant be compared > or <
dicter={"a":1,"b":2,"z":3,"o":20}
setter={"a","z","r","m","w","c","d"}
frozenSetter=frozenset(("m","a","l","n"))
stringer="prashanth"   #sortes according to ascii translations
print(sorted(lister))
print(sorted(tupler))
#print(sorted(mixedLister))
print(sorted(dicter))
print(sorted(setter))
print(sorted(frozenSetter))
print(sorted(stringer))

print("\n")
print("using join")
print("----------")
stringer="prashanth"
print("Original String:",stringer)
print("Reverse Sorted String:",sorted(stringer,reverse=True))
print("Joined Sorted String:",''.join(sorted(stringer,reverse=True)))

print("\n")
print("key parameter to sort list of strings based on length.")
print("------------------------------------------------------")
lister=["cccc","a","ddd","mmmmmm","op"]
print("Normal Sort:",sorted(lister))
print("Length Sort:",sorted(lister,key=len))

print("\n")
print("key parameter with function to sort list of numbers nearer to 50.")
lister=[50,0,100,87,25,200,32.78]
def nearerfind(n):
    return abs(n-50)
print("Numbers Near to Far for 50:",sorted(lister,key=nearerfind))
def remainderfind(n):
    return n%7
print("Numbers sort based on remainder when divided by 7:",sorted(lister,key=remainderfind))

print("\n")
print("case insensitive sort")
print("---------------------") #by default case sensitive sort will happen , upper alphabets first, lower alphabets next
lister=["a","B","d","C"]
print("Case Sensitive Default Sort:",sorted(lister))
print("Case insensitive sort:",sorted(lister,key=str.lower))

#importing functools, using reduce, lambda and sorted also can sort string, but needs to understand how it works.