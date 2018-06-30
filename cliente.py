import socket
HOST = '192.168.0.115'     									#Endereco do Servidor(IP ou DNS)
PORT = 5007            									#Porta em que a aplicacao estara "escutando"

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria um socket para conectar o cliente e o servidor
dest = (HOST, PORT)
tcp.connect(dest)										#realiza a conexao com o servidor
														#esta aplicacao enviara mensagens ao servidor no momento que enviar
														#o caractere CTRL+X(\x18 em hexadecimal) ou 
														#parar a aplicacao o servidor ira desconectar o cliente

print 'Para sair use CTRL+X\n'
msg = raw_input() 										#responsavel por receber a mensagem
while msg <> '\x18':
    tcp.send (msg)	
    msg = raw_input()									#responsavel por receber a mensagem
tcp.close()												#fecha a conexao
