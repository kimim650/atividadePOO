from bancoteste.banco_lista import Bancolista
from bancoteste.conta import Conta
from bancoteste.contapoupanca import ContaPoupanca


def main():
    # Criação dos bancos com taxas de juros
    banco1 = Bancolista("Banco 1", taxa_juros=0.05)
    banco2 = Bancolista("Banco 2", taxa_juros=0.03)
    banco3 = Bancolista("Banco 3", taxa_juros=0.02)

    # Criação das contas
    conta_lice = ContaPoupanca("lice")
    conta_jao = Conta("Jão")
    conta_jefte = ContaPoupanca("jefte")
    conta_dina = Conta("Dina")
    conta_anao = ContaPoupanca("Anao")
    conta_julie = Conta("Julie")

    # Cadastro das contas nos bancos
    banco1.cadastrar_conta(conta_lice)
    banco1.cadastrar_conta(conta_jao)
    banco2.cadastrar_conta(conta_jefte)
    banco2.cadastrar_conta(conta_dina)
    banco3.cadastrar_conta(conta_anao)
    banco3.cadastrar_conta(conta_julie)

    # Remoção de uma conta
    banco3.remover_conta("Anao")

    # Operações no Banco 1
    print("\n--- Operações no Banco 1 ---")
    banco1.creditar("lice", 7060)
    banco1.debitar("lice", 580)
    banco1.transferir("lice", "Jão", 406)
    banco1.render_juros("lice")

    # Operações no Banco 2
    print("\n--- Operações no Banco 2 ---")
    banco2.creditar("jefte", 50)
    banco2.debitar("jefte", 180)
    banco2.transferir("jefte", "Dina", 10)
    banco2.render_juros("jefte")

    # Operações no Banco 3
    print("\n--- Operações no Banco 3 ---")
    banco3.creditar("Julie", 100)
    banco3.debitar("Julie", 147.3)
    banco3.render_juros("Julie")

    # Exibição de saldos no Banco 1
    print("\n--- Saldos no Banco 1 ---")
    print(f"Saldo de lice: {banco1.saldo('lice')}")
    print(f"Saldo de Jão: {banco1.saldo('Jão')}")

    # Exibição de saldos no Banco 2
    print("\n--- Saldos no Banco 2 ---")
    print(f"Saldo de jefte: {banco2.saldo('jefte')}")
    print(f"Saldo de Dina: {banco2.saldo('Dina')}")

    # Exibição de saldos no Banco 3
    print("\n--- Saldos no Banco 3 ---")
    print(f"Saldo de Julie: {banco3.saldo('Julie')}")

    # Mensagem para conta já removida
    print("\n--- Contas removidas ---")
    print("Conta 'Anao' já foi removida ou não existe.")


if __name__ == "__main__":
    main()
