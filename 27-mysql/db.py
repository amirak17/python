# pip install mysql-connector-python
import mysql.connector

def get_connection():
    conn = mysql.connector.connect(host="localhost", user="test", password="vertic06", db="test")
    cursor = conn.cursor(buffered=True, dictionary=True)
    return cursor, conn
