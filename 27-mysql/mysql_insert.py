import db 
cursor, db = db.get_connection()

sql = 'INSERT INTO stocks (dt_stamp, closing, symbol) VALUES (%s, %s, %s)'
val = ('2021-04-20', '132132.029597', 'AAPL') # in mysql db (date, decimal, varchar)
cursor.execute(sql, val)
db.commit()

print(cursor.rowcount, "record inserted.")
