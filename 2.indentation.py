# Works, minimum 1 space for block identification required. commonly use 4 spaces i.e Tab.
if(5 > 2):
    print("5 is greater than 2.")

# Dont Work: IndentationError, no indentation for print
#if(5 > 2):
#print("5 is greater than 2.")

# Works, multiple blocks inside can be spaced accordingly
if(5 > 2):
    print("5 is greater than 2.")
    if(5 > 2):
        print("5 is greater than 2.")

# Dont works, different spaces for different statements in a single block
#if(5 > 2):
    #print("5 is greater than 2.")
    	#print("5 is greater than 2.")
