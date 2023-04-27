# -*- coding: utf-8 -*-
from socket import *

server_name = "150.162.244.37"
server_port = 9000

print("Bem vindo ao Servidor TCP!\n")

s = input("Entre com o IP do servidor (Enter para padrão): ")
i = input("Entre com a porta (Enter para padrão): ")

if (s): server_name = s
if (i): server_port = i

serv = socket(AF_INET, SOCK_STREAM)
serv.bind((server_name, int(server_port)))
serv.listen(2)

list_clients = []

for i in range(2):
    print('\nServidor aguardando!')
    conn, client_address = serv.accept()
    conn.sendall(b"" + str(i).encode()) # informar seu numero
    list_clients.append(conn)
    print(f"Conexão estabelecida com Cliente {i + 1}: {client_address}")

print("\nTudo pronto!\n")

while True:
    try:
        # Recebe dados do cliente 1
        data = list_clients[0].recv(4096)
        print(f"Recebi a data: '{data.decode('utf-8')}' do cliente 1")
        
        # Envia dados para o cliente 2
        list_clients[1].sendall(data)
        print(f"Enviei a data para o cliente 2")
        
        # Aguarda resposta do cliente 2
        data = list_clients[1].recv(4096)
        print(f"Recebi a data: '{data.decode('utf-8')}' do cliente 2")
        
        # Envia dados para o cliente 1
        list_clients[0].sendall(data)
        print(f"Enviei a data para o cliente 1")
        
    except Exception as e:
        print("Erro no servidor")
        print(e)
        list_clients[0].close()
        list_clients[1].close()
        break