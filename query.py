import sqlite3

#=============================================#
#Codigo para imprimir los mensajes por consola#
#=============================================#

conn = sqlite3.connect('chat.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM messages")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
