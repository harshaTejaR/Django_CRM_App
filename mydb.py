#install Mysql on your computer
#pip install myslq
#pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Pass@1993",
)

#prepare a cursor object using cursor() method
cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE MrH")
print("All Done!")