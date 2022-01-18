from conta import Conta
from cliente import Cliente
from data import Data

# Testando a criação de contas chamando a Classe

conta = Conta(123, "João Gilberto", 55.0, 1000.0)
conta2 = Conta(456, "Patrícia Andrade", 100.0, 1000.0)

"""
print(f"A conta de número {conta.saldo}, do titular {conta.titular}"
      f" tem um saldo de {conta.saldo} e um limite de {conta.limite}.")

print(f"A conta de número {conta2.numero}, do titular {conta2.titular}"
      f" tem um saldo de {conta2.saldo} e um limite de {conta2.limite}.")

OBS: Não é possível acessar mais os dados acima após deixar os atributos privados.

# Testando os métodos da Classe Conta

conta.extrato()
conta.depositar(100)
conta.extrato()
conta.sacar(5)
conta.extrato()

# Desafio - Criar classe Data e o método para formatar data
# Testando a classe e o método

data = Data('21', '11', '2007')
data.dataFormatada()

# Testando o método de transferência da classe Conta

conta2.transferir(50, conta)
conta.extrato()
conta2.extrato()

# Testando o Getter e o Setter

print(conta.get_limite())
conta.set_limite(10000.0)
print(conta.get_limite())

# Testando as anotações de propriedade e setter

cliente = Cliente('joão gilberto')
print(cliente.nome)

cliente.nome = 'pedro'
print(cliente.nome)

# Testando as anotações no atributo limite

print(conta.limite)
conta.limite = 5000.0
print(conta.limite)

"""








