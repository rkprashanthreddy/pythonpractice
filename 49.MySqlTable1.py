print("Create and View Tables.")
print("-----------------------")
#make sure to include database in which we are going to create the table in connection.
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="pythonpractice"
)
mycursor=mydb.cursor()
#Note:if tables already exists with same name the creation throws exception.

mycursor.execute("CREATE TABLE prashanth (name varchar(100), address varchar(100))")
print("Table created and following are the tables in the database.")
print("-----------------------------------------------------------")
mycursor.execute("SHOW TABLES")
for x in mycursor:
	print(x)

print("\n")

print("Primary key and auto increment in table creation")
print("------------------------------------------------")
mycursor.execute("CREATE TABLE friends (id int auto_increment primary key, name varchar(100))")
print("Table created and following are the tables in the database.")
print("-----------------------------------------------------------")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

print("\n")

print("Alter table.")
print("------------")
mycursor.execute("ALTER TABLE prashanth ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
print("Table Altered.")


print("\n")

print("Insert single row into table.")
print("-----------------------------")
sql="INSERT INTO prashanth (name,address) VALUES (%s,%s)" # %s used to avoid sql injection.
values=("Prashanth Reddy R K","Bengaluru")
mycursor.execute(sql,values)
mydb.commit()
print(mycursor.rowcount,"Details Added.")

print("\n")

print("Insert mulitple values into table.")
print("----------------------------------")
sql="INSERT INTO friends (name) VALUES (%s)"
values=[("Naveen",),("Saara",),("Sita",)]
mycursor.executemany(sql,values)
mydb.commit()
print(mycursor.rowcount,"Details Inserted.")
print("Last Inserted ID: ",mycursor.lastrowid)

print("\n")

print("Select from table.")
print("------------------")
mycursor.execute("SELECT * FROM friends")
myresult=mycursor.fetchall()  #fetchall() method will fetches all rows from last executed statement.
for x in myresult:
    print(x)

print("\n")

print("Select perticular columns from table")
print("------------------------------------")
mycursor.execute("SELECT name,address FROM prashanth")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

print("\n")

print("Select one record from table.")
print("-----------------------------")
mycursor.execute("SELECT * FROM prashanth")
myresult=mycursor.fetchone()   #first row will fetch
print(myresult)                #no need to loop as it contains only one row

#Note: if we put fetchone code before fetchall, fetchone will fetch data, fetchall will through internal error.