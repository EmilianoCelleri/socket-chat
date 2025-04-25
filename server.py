import socket
import sqlite3
import time

#Configurar el tipo de socket y establecer el puerto 5000
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))

def init_socket():
    '''
    Funcion para inicializar el socket
    '''   
    try:
        server_socket.listen(1)
        print("Socket inicializado esperando conexión de un cliente...")
    except:
        print("Error al inicializar el Socket")

def insert_message_intodb(contenido, fecha_envio, ip_cliente):
    '''
    Funcion para introducir los mensajes en la base de datos
    '''
    
    try:
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO messages (contenido, fecha_envio, ip_cliente) VALUES (?,?,?)", (contenido, fecha_envio, ip_cliente))

        conn.commit()
        conn.close()
    except:
        print("Error al insertar en la DB")

        




#Inicializar el socket
init_socket()


#Ciclo para aceptar las conexiones al socket
while True:
    #Aceptar la conexion del cliente y extraer la ip
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address}")
    
    try:
        #Enviar un mensaje a los clientes
        client_socket.send(b"Hola, cliente! Bienvenido al servidor.")

        #Recibir mensajes y decodificarlos
        message = client_socket.recv(1024).decode()

        #Ciclo para terminar la ejecucion con 'Exito' o 'exito'
        while message.strip().lower() != "exito" and message:
            message = client_socket.recv(1024).decode()
            respuesta = f"Mensaje recibido: {time.strftime('%Y-%m-%d %H:%M:%S')}" 
            insert_message_intodb(contenido=message,fecha_envio=time.strftime("%Y-%m-%d %H:%M:%S"),ip_cliente=client_address[0])
            client_socket.send(respuesta.encode()) 
            print(respuesta)

            
    except:
        print("Error en la comunicación con el cliente:")

    print(f"Cliente {client_address} desconectado.\n")
    client_socket.close()


