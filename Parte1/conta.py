
class Conta:

    # Implementando a função construtora em python
    def __init__(self, numero, titular, saldo, limite):
        # Implementando Atributos da classe conta
        # __ Os 2 underscores na frente dos atributos os tornam privados (Encapsulamento)
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Implementando Métodos da classe Conta
    def extrato(self):
        print(f"O saldo de {self.__titular} é de {self.__saldo}")

    def depositar(self, deposito):
        self.__saldo += deposito

    # Implementando a regra de saque à parte
    def __pode_sacar(self, saque):
        valor_disponivel = self.__saldo + self.__limite
        return saque <= valor_disponivel

    def sacar(self, saque):
        if self.__pode_sacar(saque):
            self.__saldo -= saque
        else:
            print(f"O valor de {saque} ultrapassou o limite de {self.__limite}.")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # Implementando os Getters da classe Conta
    # Aplicando as anotações
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    # Aplicando as anotações no atributo limite
    @property
    def limite(self):
        return self.__limite

    # Implementando os Setters da classe Conta
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Implemantando métodos estáticos, ou seja, métodos da classe,
    # que podem ser chamados independente da criação de um objeto
    @staticmethod
    def cod_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
