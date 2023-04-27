# -*- coding: utf-8 -*-
from socket import *

server_name = "192.168.0.103"
server_port = 9000
client_socket = socket(AF_INET, SOCK_DGRAM)

print("Bem-vindo ao Cliente UDP!\n")

s = input("Entre com o IP do servidor (Enter para localhost): ")
i = input("Entre com a porta (Enter para padrão): ")
num_client = int(input("N cliente: "))

if s:
    server_name = s
if i:
    server_port = int(i)

option_label = """
Escolha uma dessas opções:

1. Enviar mensagem ao servidor
2. Enviar mensagem a outro cliente
3. Cancelar programa

Sua escolha: """

while True:
    option = input(option_label)

    if option == "3":
        print("Programa finalizado")
        client_socket.close()
        exit()

    elif option == "1":
        while True: 
          message = input("Entre com sua mensagem: ")
          client_socket.sendto(message.encode('utf-8'), (server_name, server_port))
          msg_receive, server_address = client_socket.recvfrom(4096)
          if msg_receive:
              print("Mensagem enviada!")
              print("Mensagem recebida do servidor: ", msg_receive.decode('utf-8'))

    elif option == "2":
        msg_receive, server_address = client_socket.recvfrom(4096)
        # num_client = int(msg_receive.decode('utf-8'))
        # print("Meu número cliente:", num_client + 1, "\n")
        print("\nChat Iniciado!\n")

        while True:
            try:
                if num_client == 0:
                    message = input("Entre com sua mensagem: ")
                    client_socket.sendto(message.encode('utf-8'), (server_name, server_port))
                    msg_receive, server_address = client_socket.recvfrom(4096)
                    print("Cliente 2: ", msg_receive.decode('utf-8'))

                if num_client == 1:
                    msg_receive, server_address = client_socket.recvfrom(4096)
                    print("Cliente 2: ", msg_receive.decode('utf-8'))
                    message = input("Entre com sua mensagem: ")
                    client_socket.sendto(message.encode('utf-8'), (server_name, server_port))
            except Exception as e:
                print("Erro ao enviar/receber mensagem!", e)

    else:
        print("Opção Inválida!")