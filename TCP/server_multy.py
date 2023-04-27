# -*- coding: utf-8 -*-
from socket import *

server_name = "localhost"
server_port = 9000

print("Bem vindo ao Servidor TCP!\n")

s = input("Entre com o IP do servidor (Enter para localhost): ")
i = input("Entre com a porta (Enter para padrão): ")
c = input("Entre a quantidade de clientes: ")


if (s): server_name = s
if (i): server_port = i

serv = socket(AF_INET, SOCK_STREAM)
serv.bind((server_name, server_port))
serv.listen(5)

list_clients =[]

while c:
    print('\nServidor aguardando!\n')
    conn, client_address = serv.accept()
    print(f"Conexão estabelecida com o endereço {client_address}")
    list_clients.append(client_address)

print("Finalizado: ", list_clients)

# while True:
#     try:
#         data = conn.recv(4096)
#         print(f"Recebi a data: '{data.decode('utf-8')}'\n")
#         conn.sendto(b"Recebi sua mensagem!\n", client_address)
#     except:
#         print("Erro no servidor")
#         conn.close()
#         exit()