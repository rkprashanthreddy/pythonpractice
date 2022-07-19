print("Delete Drop Table and Database")
print("------------------------------")
import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="pythonpractice")
mycursor=mydb.cursor()

print("\n")
print("Delete from table")
print("-----------------")
sql="Delete from students where score<%s"
values=(90,)
mycursor.execute(sql,values)
mydb.commit()
print("Students below 90% deleted and remaining students:")
mycursor.execute("select * from students")
for x in mycursor:
    print(x)
# if no where condition is provided then all the details from the database erased.

print("\n")
print("Drop table")
print("----------")
mycursor.execute("drop table prashanth")
mydb.commit()
print("Table Dropped.")
print("Remaining Tables:")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

print("\n")
print("Drop table if only exists")
print("-------------------------")
mycursor.execute("DROP TABLE IF EXISTS prashanth")
mydb.commit()
#if exists helps to get rid of error when table not present in the database.s

print("\n")
print("Drop database")
print("-------------")
mycursor.execute("DROP DATABASE pythonpractice")
mydb.commit()
print("Database Dropped.")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

print("\n")
print("Drop database if exists")
print("-----------------------")
mycursor.execute("drop database if exists pythonpractice")
mydb.commit()
print("end of the program")
#commit is required in ordered to save changes to databse.

