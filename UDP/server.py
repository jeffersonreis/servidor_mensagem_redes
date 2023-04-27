# -*- coding: utf-8 -*-
from socket import *

server_name = "localhost"
server_port = 9000

print("Bem vindo ao Servidor TCP!\n")

s = input("Entre com o IP do servidor (Enter para localhost): ")
i = input("Entre com a porta (Enter para padrão): ")

if (s): server_name = s
if (i): server_port = i

serv = socket(AF_INET, SOCK_DGRAM)
serv.bind((server_name,server_port))

print('\nServidor aguardando!\n')

while True:
    try:
      data, client_address = serv.recvfrom(4096)
      print(f"Recebi a data: '{data.decode('utf-8')}' do endereço {client_address}\n")
      serv.sendto(b"Recebi sua mensagem!\n", client_address)
    except:
       print("Error server")
       exit()
