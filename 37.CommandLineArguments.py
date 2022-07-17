#argv is inbuilt list type varaible inside sys module help to capture command line arguments
#argv list contain first item as filename i.e argv[0] will be file name.
#if we print argv full list can be get.
#if we print len(argv) lenth of the list can be obtained.

print("command line arguments with sys module")
print("------------------------------------------------------")
print("Without Command Line Arguments")
print("---------------------------------------------")
number1=int(input("Enter Number 1:"))
number2=int(input("Enter Number 2:"))
total=number1+number2
print("Sum of Numbers=",total)

print("\n")
print("with command line arguments.")
print("---------------------------------------")
from sys import argv       
total=int(argv[1])+int(argv[2])
print("Sum of Numbers=",total)

print("\n")
print("printing command line arguments and length")
print("---------------------------------------------------------")
print(argv[0])
print(argv)
print(len(argv))
for x in argv:
	print(x)

print("\n")
print("summing 0 or more command line arguments.")
print("-----------------------------------------------------------")
sum=0
x=argv[1:]
for i in x:
	sum=sum+int(i)
print("Total Sum=",sum)

print("\n")
print("file merger without command line arguments.")
print("-----------------------------------------------------------")
file1=open("37.demofile1.txt")
file2=open("37.demofile2.txt")
file3=open("37.mergedfile.txt","w")
for x in file1:
	file3.write(x)
for x in file2:
	file3.write(x)
print("Files merged.")

print("\n")
print("file merger with command line arguments dynamic file names.")
print("--------------------------------------------------------------------------------")
import re
pattern1=re.search("r(\b\d+\b)?([.])?\w+[.][a-z]+",argv[1])
pattern2=re.search("r(\b\d+\b)?([.])?\w+[.][a-z]+",argv[2])
if pattern1:
    if pattern2:
        file1=open(argv[1])
        file2=open(argv[2])
        file3=open(argv[3],"w")
        for x in file1:
        	file3.write(x)
        for x in file2:
          	file3.write(x)
    else:
        print("second argument in the command line is not file name.")
else:
    print("first argument in the command line is not file name.")

print("\n")
print("check exact number of command line arguments")
print("--------------------------------------------------------------")
argscount=len(argv)-1
if argscount<3 or argscount>3:
	print("Please you have to enter 3 arguments")
else:
	print(args)

	

