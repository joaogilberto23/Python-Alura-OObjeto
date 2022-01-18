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

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # Implementando os Getters da classe Conta
    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    # Aplicando as anotações no atributo limite
    @property
    def limite(self):
        return self.__limite

    # Implementando os Setters da classe Conta
    @limite.setter
    def limite(self, limite):
        self.__limite = limite