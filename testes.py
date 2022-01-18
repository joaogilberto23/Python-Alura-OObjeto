from conta import Conta

conta = Conta(123, "João Gilberto", 55.0, 1000.0)
conta2 = Conta(456, "Patrícia Andrade", 100.0, 2000.0)

"""
print(f"\nA conta de número {conta.numero}, do titular {conta.titular}"
      f" tem um saldo de {conta.saldo} e um limite de {conta.limite}.")

print(f"\nA conta de número {conta2.numero}, do titular {conta2.titular}"
      f" tem um saldo de {conta2.saldo} e um limite de {conta2.limite}.")
"""

conta.extrato()
conta.deposito(100)
conta.extrato()
conta.saque(5)
conta.extrato()
