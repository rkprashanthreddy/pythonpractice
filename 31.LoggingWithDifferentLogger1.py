#default logger is root, but root is having one issue when dealing with multiple log files need
#to be generate in multple programs.
#root logger can be configured with basicConfig, once set,log file will be one only and all logs will
#log to that file even different log files is assigned in different files, once set root cant be override.

print("Logging With Different Logger 1")  # when imported all prints will be printed by default.
print("---------------------------------------")

import logging
#creating logger, __name__ is recomended it creates logger name as current file name
# we can use any other name as desired.
logger=logging.getLogger(__name__)
#set level with setLevel() method.
logger.setLevel(logging.DEBUG)
#create a format to be printed in log file
formating=logging.Formatter("%(levelname)s - %(name)s - %(message)s")
#assign filename to which logs can be logged.
filehandling=logging.FileHandler("DifferentLogger1.log")
#apply created format over filename
filehandling.setFormatter(formating)
#apply filename to logger
logger.addHandler(filehandling)

#now use logger than logging.
logger.info("Start Different Logging 1")
def ageCheck(age):
	if age<18:
		logger.error("Age less than 18 check")
		return "Not eligible for voting."
	elif age>18 and age<150:
		logger.debug("Age greater than 18 check")
		return "Eligible for voting."
	else:
		logger.error("Age more than 150")
		return "Eligible for voting, vote from home only peacefully."

print(ageCheck(17))
logger.info("End Different Logging 1")