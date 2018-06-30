import socket
class Conexao:
    def __init__(self, ip, porta):
        self.ip = ip
        self.porta =porta



    def servidor(self):
        self.tipo="servidor"
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (self.ip,  self.porta)
        self.tcp.bind(orig)
        self.tcp.listen(1)

    def aceitarConexao(self):
        self.con, self.cliente = self.tcp.accept()
        print 'Concetado: ', self.cliente

    def encerrarCliente(self):
        self.con.close()

    def retornarCliente(self):
        return self.con, self.cliente

    def cliente(self):
        self.tipo="cliente"
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest=((self.ip,self.porta))
        self.tcp.connect(dest)


    def enviar(self,msg):
        if("servidor" in self.tipo):
            self.con.send(msg)
        elif("cliente" in self.tipo):
            self.tcp.send(msg)

    def receber(self):
        msg = "sem conexao"
        if("servidor" in self.tipo):
            msg = self.con.recv(1024)
        elif("cliente" in self.tipo):
            msg=self.tcp.recv(1024)

        if not msg:
            return "saiu"
        return msg

    def fechar(self):
        self.tcp.close()
