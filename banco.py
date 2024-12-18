class Banco:
    def _inint_(self):
        self.contas = []

    def cadastrar(self,conta):
        if self.procurar_conta(conta.get_numero()) is None:
            self.conta.append(conta)

        else :
            print("Conta já cadastrada")


    def procurar_conta(self, numero):
        for conta in self.contas:
            if conta.get_numero()==numero:
                return conta
        return None
    
    def creditar(self,numero,valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print("Conta Não existe")

    def debitar(self,numero,valor):
        conta = self.procurar_conta(numero)
        if conta :
            if valor>0:
                if conta.get_saldo()>=valor:
                    conta.debitar(valor)
                else:
                    print("Saida não suficiente")
            else:
                print("o valor de debito precisa ser positivo")
        else:
            print("Conta não existe")
    
    def saldo(self,numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print("Conta não existe")
            return None
        
    def transferir(self,origem,destino,valor):
        conta_origem = self.procurar_conta(origem)
        conta_destino = self.procurar_conta(destino)

        if conta_origem and conta_destino:
            if conta_origem.get_saldo()>=valor:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
                
            else:
                print("Saldo insuficiente na conta de origem")

        else:
            print("Conta de origem ou destino não existe")