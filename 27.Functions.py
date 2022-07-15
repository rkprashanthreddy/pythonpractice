 print("Functions")
print("------------")
print("Normal Function:")
def printMessage():
	print("Hello Prashanth")
printMessage()

print("\n")
print("Single Parameter function defination, single argument passing: ")
def name(fullName):
	print("Hello "+fullName)
name("Prashanth Reddy")

print("\n")
print("Multi Arguments: ")
def sum(a,b):
	print(a+b)
sum(10,20)

print("\n")
print("Default Arguments: ")
def fullname(fname,lname="Reddy"):
	print("Hello "+fname+" "+lname)
fullname("Prashanth")
fullname("Prashanht","Sarkar")

print("\n")
print("* args using: ")
def students(*names): #passed as tuple of values
	print("First Student:",names[0])
students("Mani","Prashanth","Saniya")

print("\n")
print("Keyword Arguments:")
def childrens(child1,child2,child3):
	print("child1=",child1)
	print("child2=",child2)
	print("child3=",child3)
childrens(child3="Sani",child1="Mani",child2="Toni")

print("\n")
print("** kwargs using=")
def cars(**names):  #passed as dictionary
	print("First Car=",names['firstcar'])
	print("Last Car=",names['thirdcar'])
cars(firstcar="BMW",secondcar="Lamborguinni",thirdcar="Bugati")

print("\n")
print("Recurrsion Function=")  #maximum recurrsion depth=1000
def sum(n):
	total=0
	if total>100:              #base condition to stop infinite recurssion hits maximum depth
		total=total+sum(10)
	print(total)
sum(0)

print("\n")
print("List argument:")
def numers():
	pass
print("Function passed")

print("\n")
print("List Argument")
def lister(n):
	print(n)
x=[1,2,3,4,5]
lister(x)

print("\n")
print("Multiple Function Calls:")
def printmulti():
	print("Hello World")
printmulti()
printmulti()
printmulti()

print("\n")
print("Return Functions:")
def sum(a,b):
	return a*b
x=sum(10,20)
print(x)

print("\n")
print("Recurrsion Function To Find Out Factiorial")
print("------------------------------------------")
def factorial(n):
	if n==1:
		return 1
	else:
		return (n*factorial(n-1))
print("Factorial of 10:",factorial(10))

print("\n")
print("Factorial finding without recurrsion function")
def factorial(n):
	factorial=1
	if n==1:
		return 1
	else:
		for i in range(1,n+1):
			factorial=factorial*i
	return factorial 
print("Factorial of 10:",factorial(10))

print("\n")
print("Lambda Function:")
print("----------------")
#small anonymous function, args can be n number but expression should be 1
x=lambda a:a+10
print("One Arg Simple Lamda:",x(10))
x=lambda a,b:a*b
print("Dual Args Lambda:",x(10,20))
x=lambda a,b,c:a+b+c
print("Multi Args Lambda:",x(10,20,30))

print("\n")
print("Power Of Lambda")
print("---------------")
#can be observed when used inside functions
def dual(n):
	return lambda a:a*n 
doubler=dual(2)
tripler=dual(3)
print(doubler(10))
print(tripler(20))
# can be used when anonymous function required for short period of time.

