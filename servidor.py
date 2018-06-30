from conexao import Conexao
import serial
arduino = serial.Serial('COM7',9600)
servidor = Conexao("",5000)
servidor.servidor()
servidor.aceitarConexao()

while True:
    msg=servidor.receber()
    arduino.write(msg)
    # resp = (arduino.readline().strip())
    #dados = resp.decode('utf-8')
    #print dados
    if "sair" in msg:
        servidor.enviar("ate mais")
        break
    servidor.enviar(msg)

print 'Finalizando conexao do cliente'
servidor.fechar()
