print("Exception Handling")
print("------------------------")
print("Simple try except finally")
try:
	a=0
	b=20
	c=b/a
	print(c)
except:
	print("Division By Zero is not possible.")
finally:  #its optional to use, it displays after try catch regardless of try fail or success.
	print("Try completed")

print("\n")
print("except possible error")
try:
    c=b/a
    print(c)
except ZeroDivisionError:
    print("Not Possible To Divide with 0.")

print("\n")
print("except other error rather than possible error.")
try:
    c=b/a
    print(c)
#except TypeError:  #this leads to termination of program with zero divison error since its not handled.
except:
    print("Not Possible To Divide with 0.")
finally:
    print("Not Possible To Divide with 0.")

print("\n")
print("multiple excepts")
try:
    c=b/a
    print(c)
except TypeError:  #if you use only this except leads to termination of program with zero divison error its not handled.
    print("Not Possible To Divide with 0.")
except:            #its can ba used to capture all other exceptions.
    print("Error Dividing With 0.")

print("\n")
print("Multiple possible errors")
try:
    c=b/a
    print(c)
except (TypeError,ZeroDivisionError):
    print("0 can not be used to divide.")

print("\n")
print("nested try except")
try:
    file=open("hello.txt")
    try:
        file.write("Hello Prashanth.")
    except:
        print("Write permission is not given.")
    finally:
        file.close()
except:
    print("file does not exhist to open.")

print("\n")
print("try except else finally")
x=10
try:
    print(x)
except NameError:
    print("X is not defined.")
else:
    print("Nothing went wrong.")
finally:
    print("test completed.")

print("\n")
print("empty try except")
try:
    pass
except:
    pass
print("try except passed.")

print("\n")
print("raise general exception")
x=-1
#if x<0:
    #raise Exception("Less than zero.")
print("uncomment to see exception, it will stop further execution of the program.")

print("\n")
print("raise desired exception")
x="Hello"
#if not type(x) is int:
    #raise TypeError("Its not int.")
print("uncomment to see exception, it will stop further execution of the program.")

"""
common exceptions or errors
---------------------------
1. ValueError: if value have problem
2. SyntaxError: if syntax mistake by developer
3. IndexError: if list or any index is out of range
4. IOError: if input or output error
5. ImportError: if error while importing module
6. ZeroDivisionError: if try to divide number by 0
7. NameError: if name of variable anything is having wrong
8. TypeError: if types mismatch
9. KeyboardInterruptError: occurs when pressed by cntrl+c etc
10. EOFError: end of file error.
"""