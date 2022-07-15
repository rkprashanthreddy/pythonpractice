import logging  
print("Logging Levels:5")
print("---------------------")
logging.basicConfig()
logging.info("Program started") # info for general information used.
def nameCheck(name):
    if len(name) < 2:
        logging.error("Checking for name length.") #error for general error but no program quit.
        return "Invalid Name."
    elif name.isdigit():
        logging.error("Checking for name is an digit.")
        return "Invalid Name."
    elif name.isalpha():
        logging.debug("Checking for name is an alphabet.")  #debug for general details.
        return "Valid Name."
    elif name.isalnum():
        logging.warning("Checking Digits and alphabets mixed.") #warning for may not problem quit in future or may quit.
        return "Invalid Name"
    else:
        logging.critical("All Checks Failed.") #critical for where there is a chance of program quit.
        return "Invalid Name."


print(nameCheck("123s"))
logging.info("Program ended")