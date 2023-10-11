# pip install mysql-connector-python
import mysql.connector

db = mysql.connector.connect(host="localhost", user="test", password="pwd", database="test")
cursor = db.cursor(buffered=True, dictionary=True)

sql = 'SELECT * FROM stocks'
cursor.execute(sql)
rows = cursor.fetchall()

# all rows
for i in range(0, len(rows)):
    print(rows[i]['symbol'])

# first Element
print(rows[0]['symbol'])
