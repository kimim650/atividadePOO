from bancoteste.contapoupanca import ContaPoupanca

class Bancolista:
    def __init__(self, nome: str, taxa_juros: float = 0.1):
        if not nome or not isinstance(nome, str):
            raise ValueError("O nome do banco deve ser uma string não vazia.")
        if taxa_juros < 0:
            raise ValueError("A taxa de juros não pode ser negativa.")

        self.nome = nome
        self.contas = []
        self.taxa_juros = taxa_juros

    def cadastrar_conta(self, conta: ContaPoupanca) -> None:
        if self.procurar_conta(conta.get_numero()) is None:
            self.contas.append(conta)
            print(f"Conta {conta.get_numero()} cadastrada no banco {self.nome}.")
        else:
            print(f"Conta {conta.get_numero()} já cadastrada no banco {self.nome}.")

    def procurar_conta(self, numero: int):
        for conta in self.contas:
            if conta.get_numero() == numero:
                return conta
        return None

    def creditar(self, numero: int, valor: float) -> None:
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
            print(f"Valor de R${valor} creditado na conta {numero}.")
        else:
            print(f"Conta {numero} não encontrada no banco {self.nome}.")

    def debitar(self, numero: int, valor: float) -> None:
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
            print(f"Valor de R${valor} debitado da conta {numero}.")
        else:
            print(f"Conta {numero} não encontrada no banco {self.nome}.")

    def saldo(self, numero: int) -> float:
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print(f"Conta {numero} não encontrada no banco {self.nome}.")
            return None

    def listar_contas(self) -> None:
        if not self.contas:
            print(f"Nenhuma conta registrada no banco {self.nome}.")
        else:
            print(f"Contas do banco {self.nome}:")
            for conta in self.contas:
                print(f"Conta {conta.get_numero()} - Saldo: {conta.get_saldo()}")

    def transferir(self, origem: int, destino: int, valor: float) -> None:
        conta_origem = self.procurar_conta(origem)
        conta_destino = self.procurar_conta(destino)

        if conta_origem and conta_destino:
            if conta_origem.get_saldo() >= valor:
                conta_origem.debitar(valor)
                conta_destino.creditar(valor)
                print(f"Transferência de R${valor} realizada de {origem} para {destino}.")
            else:
                print("Saldo insuficiente na conta de origem!")
        else:
            print("Conta de origem ou destino inexistente!")

    def render_juros(self, numero: int) -> None:
        conta = self.procurar_conta(numero)
        if isinstance(conta, ContaPoupanca):
            conta.render_juros(self.taxa_juros)
            print(f"Juros aplicados à conta {numero}.")
        else:
            print(f"Conta {numero} não é uma conta poupança ou não existe no banco {self.nome}.")

    def remover_conta(self, numero: int) -> None:
        conta = self.procurar_conta(numero)
        if conta:
            self.contas = [c for c in self.contas if c.get_numero() != numero]
            print(f"Conta {numero} removida do banco {self.nome}.")
        else:
            print(f"Conta {numero} não encontrada no banco {self.nome}.")