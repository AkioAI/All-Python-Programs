# create a database named “PythonDatabase"
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="@Kanime211")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE PythonDatabase")