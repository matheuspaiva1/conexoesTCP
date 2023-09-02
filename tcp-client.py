############################### CONEXÕES PADRÃO ###########################################
import socket

host = 'localhost'
port = 12345

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((host, port))
###########################################################################################

################################ CODIGO APLICAÇÃO ##########################################
num1, num2 = map(float, input("digite dois numeros separados por espaço").split())

clientSocket.send(f"{num1} {num2}".encode())

result = clientSocket.recv(1024).decode()

print(f"resulado da soma: {result}")

clientSocket.close()

