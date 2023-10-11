import db 
cursor, db = db.get_connection()

sql = 'SELECT * FROM stocks'
cursor.execute(sql)
rows = cursor.fetchall()

# all rows
for i in range(0, len(rows)):
    print(rows[i]['symbol'])

# first Element
# print(rows[0]['symbol'])