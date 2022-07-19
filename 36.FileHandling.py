print("File Handling")
print("-----------------")

print("\n")
print("create file with 'x'.")
print("----------------")
#file=open("36.demofile.txt","x")
#create empty file only if not exists, if exists gives error , write and append dont give error.

print("\n")
print("open to read with 'r' or with out 'r'.")
print("--------------------------------------")
try:
    file=open("36.demofile.txt")           #opening with defualt read mode, if not exist file gives error.
    file.close()
except:
    print("file not exists.")
# same as open("36.demofile.txt","r")
#file.write("hello")                #gives error as its not open to write.

#in write and append case if the file does not exists it will create and write or append content
print("\n")
print("write to file with 'w'.")
print("----------------")
file=open("36.demofile.txt","w")  # write permission overwrite the content of the file.
file.write("Hello prashanth how are you, \n i am fine thank you.")
file.close()

print("\n")
print("append to file with 'a'.")
print("----------------")
file=open("36.demofile.txt","a")  # appends content at last of the file
file.write("\nHello prashanth how are you, \n i am fine thank you.")
file.close()

print("\n")
print("Read Entire File.")
print("---------------------")
file=open("36.demofile.txt")
print(file.read())                       #read entire file.
file.close()

print("\n")
print("Read line by line File.")
print("---------------------------")
file=open("36.demofile.txt","r")
print(file.readline())
print(file.readline())   #more than existing lines try to read leads to nothing,
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

print("\n")
print("Read by characters.")
print("------------------------")
file=open("36.demofile.txt")
print(file.read(5))  #read upto 5th character.
print(file.read())   #reads after 5th position to end of document.
file.close()

print("\n")
print("loop through the lines of the file.")
print("-----------------------------------")
file=open("36.demofile.txt")
for x in file:
    print(x)
#file.close()  even for looped we dont close also os.remove works

print("\n")
print("closing the file after use")
print("--------------------------")
file=open("36.demofile.txt")
print(file.readline())
file.close()
print("file closed.")

print("\n")
print("text and binary mode")
print("--------------------")
file=open("36.demofile.txt","rt")  # t for text file, b for images.
file=open("36.demofile.txt","rb")   # b for binary. only t or b cant be given it should be wb or rb etc
# if we used 'wb' then file opens for write and writes empty, so file remains empty after creation.
file.close()

print("\n")
print("open file in other path")
print("-----------------------")
try:
    file=open("/html/doc/hello.txt")  #provide full path
    file.close()
except:
    print("not there that file.")


print("\n")
print("remove file")
print("------------")
import os  # need to import os module to remove
#os.remove("36.demofile.txt")
#print("file removed.")#if any where we dint wrote file.close() that means that file still opened, those cant removable.

print("\n")
print("remove file if exists only") # check to avoid getting error while removing.
print("--------------------------")
if os.path.exists("hiding.txt"):
    os.remove("hiding.txt")
else:
    print("That file not exists to remove.")

print("\n")
print("only we can delete empty folders.")
print("---------------------------------")
#os.rmdir("foldername")

print("\n")
print("auto close file using with open")
print("-------------------------------")
#smoother way to handle files or cleaner way to handle files.
with open("36.withfile.txt","w+") as file:  #w+ for read write, r+ for read write, a+ for read append modes.
#w+ observed not work as expected. below code dint wrote to file but not read from file.
    lister=["Hello prashanth\n","I am fine thank you\n","How do you do\n"]
    file.writelines(lister)   #writelines for mulitple values, with write list cant accepted.
    print(file.read()) #read fully
    #once read by all from above line, remaining reads returns empty values.
    print(file.read(5)) #read upto 5th character
    print(file.readline()) #read single line
    print(file.readlines()) # read all lines
