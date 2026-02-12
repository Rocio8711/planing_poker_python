import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="pokerbdd"
)

print("Conectado correctamente")
conn.close()