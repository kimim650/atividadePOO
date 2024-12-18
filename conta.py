class Conta:
    def _init_(self, numero):
        self._numero =numero
        self.__saldo =0

    def creditar(self,valor):
        if valor>0:
            self.__saldo += valor
        else:
            print("O valor para ser creditado deve se positivo")
    def debitar(self,valor):
        if valor > 0:
            if self.__saldo >=valor:
                self.__saldo -=valor
            else:
                print("O valor pra debitar deve ser positivo")
    def get_numero(self):
        return self.__numero
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, saldo):
        if saldo >=0:
            self.__saldo = saldo
        else:
            print("O saldo não pode ser negativo")
