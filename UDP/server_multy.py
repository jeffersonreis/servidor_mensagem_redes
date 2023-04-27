# -*- coding: utf-8 -*-
from socket import *

# server_name = "localhost"
server_name = "150.162.244.37"
server_port = 9000

print("Bem vindo ao Servidor UDP!\n")

s = input("Entre com o IP do servidor (Enter para padrão): ")
i = input("Entre com a porta (Enter para padrão): ")

if (s): server_name = s
if (i): server_port = i

serv = socket(AF_INET, SOCK_DGRAM)
serv.bind((server_name, int(server_port)))

list_clients = []

for i in range(2):
    print('\nServidor aguardando!')
    data, client_address = serv.recvfrom(4096)
    serv.sendto(str(i).encode(), client_address)  # informar seu número
    list_clients.append(client_address)
    print(f"Conexão estabelecida com Cliente {i + 1}: {client_address}")

print("\nTudo pronto!\n")

while True:
    try:
        # Recebe dados do cliente 1
        data, addr = serv.recvfrom(4096)
        print(f"Recebi a data: '{data.decode('utf-8')}' do cliente 1")

        # Envia dados para o cliente 2
        serv.sendto(data, list_clients[1])
        print(f"Enviei a data para o cliente 2")

        # Aguarda resposta do cliente 2
        data, addr = serv.recvfrom(4096)
        print(f"Recebi a data: '{data.decode('utf-8')}' do cliente 2")

        # Envia dados para o cliente 1
        serv.sendto(data, list_clients[0])
        print(f"Enviei a data para o cliente 1")

    except Exception as e:
        print("Erro no servidor")
        print(e)
        break
