class ContaBancaria:
    def __init__(self):
        self.__saldo = 0.0  # Atributo "privado" (Name Mangling)

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f" Depósito de R${valor:.2f} realizado.")
        else:
            print(" Erro: O valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print(" Erro: O valor de saque deve ser positivo.")
        elif valor > self.__saldo:
            print(f" Erro: Saldo insuficiente. Seu saldo é R${self.__saldo:.2f}")
        else:
            self.__saldo -= valor
            print(f" Saque de R${valor:.2f} realizado.")

    def ver_saldo(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")

# --- Testes ---
minha_conta = ContaBancaria()
minha_conta.depositar(100.0)
minha_conta.sacar(150.0)  # Tentativa inválida (Saldo insuficiente)
minha_conta.sacar(-10.0)  # Tentativa inválida (Valor negativo)
minha_conta.sacar(50.0)
minha_conta.ver_saldo()

# Tente descomentar a linha abaixo para ver o erro de acesso direto:
# print(minha_conta.__saldo)
