#importing other module.

print("Logging With Different Logger 2")
print("------------------------------------------")

import logging
import LoggingWithDifferentLogger1 as LWDL1
logger=logging.getLogger("prashanth")
logger.setLevel(logging.DEBUG)
formating=logging.Formatter("%(levelname)s - %(name)s - %(message)s")
filehandling=logging.FileHandler("DifferentLogger2.log")
filehandling.setFormatter(formating)
logger.addHandler(filehandling)
logger.info("Start Different Logging 2")
LWDL1.ageCheck(17)
logger.info("End Different Logging 2")