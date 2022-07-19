print("MySQL Joins")
print("-----------")
import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="pythonpractice"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE if not exists users(id int, name varchar(100), address varchar(100))")
mycursor.execute("CREATE TABLE if not exists products(id int, name varchar(100), manufactured varchar(100))")
print("Tables Created.")
sql="INSERT INTO users(id,name,address) values (%s,%s,%s)"
values=[(1,"Manish","Hyderabad"),
        (2,"Sukesh","Banglore"),
        (3,"Ramesh","Mumbai")]
mycursor.executemany(sql,values)
mydb.commit()
print(mycursor.rowcount,"Details Inserted into users")
sql="INSERT INTO products(id,name,manufactured) values (%s,%s,%s)"
values=[(1,"Preetesh","Hyderabad"),
        (2,"Manjesh","Trivendram"),
        (6,"Shandesh","Mumbai"),
        (5,"Sampesh","Madras")]
mycursor.executemany(sql,values)
mydb.commit()
print(mycursor.rowcount,"Details Inserted inserted into products")

print("\n")
print("SQL INNER JOIN or JOIN ")
print("-----------------------")
#inner join and join gives same result
sql="select users.name,products.name from users inner join products on users.id=products.id"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

print("\n")
print("SQL LEFT JOIN")
print("-------------")
sql="select users.name, products.name from users left join products on users.id=products.id"
mycursor.execute(sql)
for x in mycursor:
    print(x)

print("\n")
print("SQL RIGHT JOIN")
print("--------------")
sql="select users.name, \
     products.name from \
     users right join products \
     on users.id=products.id"
mycursor.execute(sql)
for x in mycursor:
    print(x)
