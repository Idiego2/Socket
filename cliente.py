from conexao import Conexao

cliente = Conexao("localhost",5000)
cliente.cliente()

while True:
    msg = raw_input("Digite uma msg: ")
    cliente.enviar(msg)
    resposta = cliente.receber()
    if "sair" in msg:
        break
    print resposta

cliente.fechar()
