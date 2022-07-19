import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythonpractice"
    )

mycursor=mydb.cursor()

mycursor.execute("""CREATE TABLE students
                    (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        fullname varchar(100),
                        score int
                    )
                 """)
print("Table created.")

sql="INSERT INTO students (fullname,score) values (%s,%s)"
values=[("Ramu",98),
        ("Geeta",90),
        ("Vinay",99),
        ("sangeetha",80),
        ("smitha",89),
        ("Reetha",85)]
mycursor.executemany(sql,values)
mydb.commit()
print(mycursor.rowcount,"Details Inserted")
print("filter with where and like")
print("\n")
print("Where condition in sql")
print("----------------------")
mycursor.execute("SELECT fullname,score FROM students WHERE score>90")
myresult=mycursor.fetchall()
print("Students above 90% score.")
for x in myresult:
    print(x)

print("\n")
print("Using wildcard charcaters.")
print("--------------------------")
mycursor.execute("SELECT fullname FROM students WHERE fullname LIKE '%eet%'")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

print("\n")
print("SQL Injection avoid")
print("-------------------")
sql="SELECT fullname from students where score<%s"
values=(90,)
mycursor.execute(sql,values)
print("Students below 90% score.")
for x in mycursor:
    print(x)

print("\n")
print("sorting with order by")
print("ORDER BY Use")
print("------------")
mycursor.execute("select * from students order by score")
myresult=mycursor.fetchall()
print("All Students Details.")
for x in myresult:
    print(x)

print("\n")
print("Order by ascending or descending.")
print("--------------------------------")
#ascending is by default, for descending use DESC
mycursor.execute("select * from students order by score desc")
myresult=mycursor.fetchall()
print("Descending")
for x in myresult:
    print(x)

print("\n")
print("Limit first 3 records")
print("---------------------")
mycursor.execute("select * from students limit 3")
for x in mycursor:
    print(x)

print("\n")
print("limit and offset")
print("----------------")
#offset sets start postion of records to limit
mycursor.execute("select * from students limit 3 offset 2") #from 2nd row to following 3 rows
for x in mycursor:
    print(x)

#fetchall can be used for select , but observed without fetchall also we can select.

print("\n")
print("update table")
print("------------")
sql="update students set score=%s where fullname=%s"  #without placeholders also can be used, here for saftey used.
#%s used for escape values and to avoid sql injection common technique used by hackers to attack database.
values=(98,"smitha")
mycursor.execute(sql,values)
mydb.commit()
print("details after change")
mycursor.execute("select * from students")
for x in mycursor:
    print(x)


