from socket import *
serv = socket(AF_INET, SOCK_DGRAM)
serv.bind(('localhost', 9000))
while True:
    try:
      print('\nServidor escutando!')
      data, client_address = serv.recvfrom(4096)
      print(f"Recebi a data: '{data.decode('utf-8')}' do endereço {client_address}")
      serv.sendto(b"Mensagem recebida pelo servidor!\n", client_address)
    except:
       print("Error server")
       exit()
