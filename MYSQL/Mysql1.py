# Create Connection
# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211")
# print(mydb)

# Create Database
# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211")
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE pythondatabase ")

# Checks if Database Exists
# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211")
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)




# Creating a Table
# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211",database="PythonDatabase")
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE employees(name VARCHAR(255), address VARCHAR(255))")


# Check if Tables exists
# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211",database="PythonDatabase")
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)



# Insert into a Table:-  Note: statement mydb.commit() is required to make the changes, otherwise no changes are
# made to the table.

# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211",database="PythonDatabase")
# mycursor = mydb.cursor()
# sql = "INSERT INTO employees (name, address) VALUES (%s, %s)"
# val = ("Vijay", "Highway 51")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")


# Insert Multiple row

# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211",database="PythonDatabase")
# mycursor = mydb.cursor()
# sql = "INSERT INTO employees(name, address) VALUES (%s, %s)"
# val = [('Peter', 'Lowstreet 4'),('Amy', 'Apple st 652'),('Betty', 'Green Grass 1'),('Richard', 'Sky st 331'),
#       ('Susan', 'One way 98'),('Vicky', 'Yellow Garden 2'),('Ben', 'Park Lane 38'),('William', 'Central st 954'),
#       ('Chuck', 'Main Road 989'),('Viola', 'Sideway 1633')]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")

# Using fecthall() Method to call all rows

# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211",database="PythonDatabase")
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM employees")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# using fetchone() Method to call one Row

# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211",database="PythonDatabase")
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM employees")
# myresult = mycursor.fetchone()
# print(myresult)

# using "DELETE FROM" statement to delete records
# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211",database="PythonDatabase")
# mycursor = mydb.cursor()
# sql = "DELETE FROM employees WHERE address = 'Lowstreet 4 '"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# Update Table

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211",database="PythonDatabase")
mycursor = mydb.cursor()
sql = "UPDATE employees SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")`