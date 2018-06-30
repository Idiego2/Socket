# -*- coding: utf-8 -*-
import socket
import serial
arduino = serial.Serial('COM5',9600)
HOST = ''              					# Endereco IP do Servidor
PORT = 5003         					# Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria um socket para conectar o cliente e o servidor
orig = (HOST, PORT)
tcp.bind(orig)					        #coloca o endereço local, o IP e a porta no socket
tcp.listen(1)						#esta função faz com que o servidor fique no modo passivo, esperando conexões
while True:
    con, cliente = tcp.accept()				#aceita uma nova conexão
    print 'Concetado: ', cliente			#informa o IP do cliente
    while True:					        #neste while obriga o servidor a ficar no loop enquanto houver dados para receber
        msg = con.recv(1024)
        if not msg:
            break

        print cliente, msg
        arduino.write(msg)
       # resp = (arduino.readline().strip())
       # dados = resp.decode('utf-8')
    
        
        
    print 'Finalizando conexao: ', cliente



    
    con.close()
