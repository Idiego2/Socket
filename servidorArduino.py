from conexao import Conexao
import serial

servidor = Conexao("",5000)
servidor.servidor()

# arduino = serial.Serial('/dev/ttyUSB1',9600)

while True:
    print "entrar"
    servidor.aceitarConexao()
    while True:
        print "entrou"
        msg=servidor.receber()
        if 'saiu' in msg:
            print "saindo"
            break
        elif "l" in msg:
            # arduino.write(msg)
            # mydata = (arduino.readline().strip())
            # dados = mydata.decode('utf-8')
            dados = "1|2|3|4"
            print dados
            servidor.enviar(dados)
        elif "a" in msg:
            print msg
            # arduino.write(msg)
        elif "s" in msg:
            print msg
            # arduino.write(msg)
    servidor.encerrarCliente()
    print 'Finalizando conexao do cliente'

servidor.fechar()

