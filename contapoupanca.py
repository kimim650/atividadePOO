from bancoteste.conta import Conta


class ContaPoupanca(Conta):


    def _init_(self, numero):
        super()._init_(numero)
    def render_juros(self, taxa):
        if taxa > 0:
            juros = self.get_saldo() * taxa
            self.creditar(juros)
            print(f"Juros de R${juros:.2f} aplicados à conta {self.get_numero()}.")
        else:
            print("A taxa de juros deve ser positiva!")