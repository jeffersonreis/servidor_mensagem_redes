from socket import *

serv = socket(AF_INET, SOCK_STREAM)
serv.bind(('localhost', 9000))
serv.listen(5)

while True:
    try:
        print('\nServidor escutando!')
        conn, client_address = serv.accept()
        print(f"Conexão estabelecida com o endereço {client_address}")
        data = conn.recv(4096)
        print(f"Recebi a data: '{data.decode('utf-8')}'")
        conn.sendall(b"Mensagem recebida pelo servidor!\n")
        conn.close()
    except:
        print("Erro no servidor")
        exit()
