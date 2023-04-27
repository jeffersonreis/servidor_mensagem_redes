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

print('\nServidor aguardando!\n')

while True:
    try:
        data, client_address = serv.recvfrom(4096)
        print(f"Recebi a data: '{data.decode('utf-8')}'\n")
        serv.sendto(b"Recebi sua mensagem!\n", client_address)
    except:
        print("Erro no servidor")
        exit()
