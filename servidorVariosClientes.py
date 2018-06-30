import os

from conexao import Conexao
import serial

servidor = Conexao("",5003)
servidor.servidor()

# arduino = serial.Serial('/dev/ttyUSB1',9600)

while True:
    print "entrar"
    servidor.aceitarConexao()
    con, cliente = servidor.retornarCliente()
    pid = os.fork()
    print pid
    if pid == 0:
        servidor.fechar()
        while True:
            msg=con.recv(1024)
            print msg
            if not msg:
                print "saindo"
                break
            elif "l" in msg:
                # arduino.write(msg)
                # mydata = (arduino.readline().strip())
                # dados = mydata.decode('utf-8')
                dados = "1|2|3|4"
                print dados
                con.send(dados)
            elif "a" in msg:
                print msg
                # arduino.write(msg)
            elif "s" in msg:
                print msg
                # arduino.write(msg)
        con.close()
        #servidor.encerrarCliente()
        print 'Finalizando conexao do cliente'

servidor.fechar()

