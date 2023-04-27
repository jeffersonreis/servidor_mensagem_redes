from socket import *
server_name = "localhost"
server_port = 9000
timeout = 10

print("Bem vindo ao Cliente TCP!\n")

s = input("Entre com o IP do servidor (Enter para localhost): ")
i = input("Entre com a porta (Enter para padrão): ")

if s:
    server_name = s
if i:
    server_port = int(i)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.settimeout(timeout)

print("Servidor Configurado!")

try:
    client_socket.connect((server_name, server_port))
    print("Conexão estabelecida com o servidor!")
except:
    print("Erro ao conectar com o servidor!")
    client_socket.close()
    exit()

option_label = """
Escolha uma dessas opções:

1. Enviar uma mensagem
2. Cancelar programa

Sua escolha: """

while True:
    option = input(option_label)
    if option == "2":
        print("Programa finalizado")
        client_socket.close()
        exit()

    elif option == "1": 
        message = input("Entre com sua mensagem: ").encode('utf-8')
        try:
            client_socket.send(message)
            msg_receive = client_socket.recv(4096)
            if msg_receive:
                print("Mensagem enviada!")
                print("Mensagem recebida do servidor: ", msg_receive.decode('utf-8'))
        except timeout:
            print("Tempo limite excedido")
        except Exception as e:
            print("Erro ao enviar/receber mensagem!", e)
    else:
        print("Opção Inválida!")
