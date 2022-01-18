class Conta:

    # init é a função construtora em python
    def __init__(self, numero, titular, saldo, limite):

        # atributos da classe conta
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    # Métodos da classe Conta
    def extrato(self):
        print(f"O saldo de {self.titular} é de {self.saldo}")

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor
