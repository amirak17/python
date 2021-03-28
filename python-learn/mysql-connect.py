
# pip3 install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="vertic06",
  database="test"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tokens")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
