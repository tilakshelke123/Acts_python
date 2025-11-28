import mysql.connector

mydb = mysql.connector.connect(
 host="127.0.0.1",
 port="3306",
 user="root",
 password="root",
 database="mysql"
)



cursor = mydb.cursor()

cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("INSERT INTO employees VALUES (3, 'Pratiksha1', 'Harshe1', '2026-10-11');")

cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()
for row in rows:
    print(row)

mydb.commit()
mydb.close()
clear()
