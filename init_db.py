import sqlite3

#=============================#
#Codigo para inicializar la DB#
#=============================#


conn = sqlite3.connect('chat.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               contenido TEXT NOT NULL,
               fecha_envio DATE,
               ip_cliente TEXT)                
               ''')

conn.commit()
conn.close()