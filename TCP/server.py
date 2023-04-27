# -*- coding: utf-8 -*-
from socket import *

server_name = "localhost"
# server_name = "150.162.244.37"
server_port = 9000

print("Bem vindo ao Servidor TCP!\n")

s = input("Entre com o IP do servidor (Enter para padrão): ")
i = input("Entre com a porta (Enter para padrão): ")

if (s): server_name = s
if (i): server_port = i

serv = socket(AF_INET, SOCK_STREAM)
serv.bind((server_name, int(server_port)))
serv.listen(1)

print('\nServidor aguardando!\n')
conn, client_address = serv.accept()
print(f"Conexão estabelecida com o endereço {client_address}")
while True:
    try:
        data = conn.recv(4096)
        print(f"Recebi a data: '{data.decode('utf-8')}', de {client_address}\n")
        conn.sendall(b"Recebi sua mensagem!\n")
    except:
        print("Erro no servidor")
        conn.close()
        exit()