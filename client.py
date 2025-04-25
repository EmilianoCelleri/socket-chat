import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 5000))

message = client_socket.recv(1024)
print(f"Recibido del servidor: {message.decode()}")
client_socket.send(b"Hola, servidor! Soy el cliente.")

while message.strip().lower() != 'exito':
    #Enviar mensajes
    message = input("Enviar mensaje: ")
    client_socket.send(message.encode())


