############################### CONEXÕES PADRÃO ###########################################
import socket

host = 'localhost'
port = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((host, port))

serverSocket.listen(1)
print(f"Servidor aguardando conexões em {host}:{port}...")
##########################################################################################

################################ CODIGO APLICAÇÃO ###########################################
while True:
  ########### PADRÃO ####################
  clientSocket, clientAddress = serverSocket.accept()
  print(f"Conexão estabelecida com {clientAddress}")
  #######################################

  data = clientSocket.recv(1024).decode()
  nums = data.split()
  if len(nums) == 2:
    num1, num2 = float(nums[0]), float(nums[1])
    result = num1 + num2
    print(f"Soma de {num1} e {num2} é {result}")

    clientSocket.send(str(result).encode())
  else:
      client_socket.send("Erro: Forneça dois números separados por espaço.".encode())

  # Fecha a conexão com o cliente
  clientSocket.close()


