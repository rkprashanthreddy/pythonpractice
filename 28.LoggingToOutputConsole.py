# logging helps to debug program with out print statements, it logs message to console.
# usefull to findout which part of code executed , also while deliver to client can be disabled easily
# in case of print while deliver needs to be removed all prints used for testing.
# unlike print statement only prints info to output, we can log messages to log file is 2nd benifit.

import logging  # logging module needs to be imported
print("Logging")
print("--------------")
# 5 levels , DEBUG is lowest, print basic details
logging.basicConfig(level=logging.DEBUG)
#logging.disable()   #use to disable logging while deliver, but for prints we need to delete all manually
# without logging
def nameCheck(name):
    if len(name) < 2:
        print("Checking for name length.")
        # multiple same invalid names exists, to know which invalid is worked we use debugging.
        return "Invalid Name."
    elif name.isdigit():
        print("Checking for name is an digit.")
        return "Invalid Name."
    elif name.isalpha():
        print("Checking for name is an alphabet.")
        return "Valid Name."
    elif name.isalnum():
        print("Checking Digits and alphabets mixed.")
        return "Invalid Name"
    else:
        print("All Checks Failed.")
        return "Invalid Name."

print("With Print:")
print("------------")
print(nameCheck("prashanth"))
print("\n")

#with logging gives with level of logging and logger information also, here level is debug and defualt logger is root.
def nameCheck(name):
    if len(name) < 2:
        logging.debug("Checking for name length.")
        # multiple same invalid names exists, to know which invalid is worked we use debugging.
        return "Invalid Name."
    elif name.isdigit():
        logging.debug("Checking for name is an digit.")
        return "Invalid Name."
    elif name.isalpha():
        logging.debug("Checking for name is an alphabet.")
        return "Valid Name."
    elif name.isalnum():
        logging.debug("Checking Digits and alphabets mixed.")
        return "Invalid Name"
    else:
        logging.debug("All Checks Failed.")
        return "Invalid Name."

print("With Logging:")
print("-------------")
print(nameCheck("123s"))
