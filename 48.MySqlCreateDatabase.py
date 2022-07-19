print("Create and View Databases")
print("----------------------------------")
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE pythonpractice")
print("database created, the following are the databases present in the mysql.")
print("-----------------------------------------------------------------------------------------")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
	print(x)
