#filemode is set to write as defualt will be append.
#format applied how the log need to be printed. file name not required to be .log it can also be txt file.

print("Logging To File")
print("--------------------")
import logging
logging.basicConfig(filename="LogingToFileDemo.log",level=logging.DEBUG,filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
def operatorCheck(operator):
	if operator=="+":
		logging.debug("addition comparison")
		return "It is an operator."
	elif operator=="-":
		logging.debug("substraction comparision")
		return "It is an operator."
	elif operator=="*":
		logging.debug("Multiplication comparision.")
		return "It is an operator."
	elif operator=="/" or operator=="//":
		logging.debug("Division comparision.")
		return "It is an operator."
	elif operator=="%":
		logging.debug("modulus comparision.")
		return "it is an operator."
	elif operator=="**":
		logging.debug("power comparision.")
		return "it is an operator."
	else:
		logging.debug("no match")
		return "No. it is not an operator."

print(operatorCheck("//"))