class Conta:
    def __init__(self):
        self.titular = ""
        self.numero = ""
        self.saldo = 0
    def depositar(self, valor):
        self.saldo = self.saldo + valor
    def sacar(self, valor):    
        self.saldo = self.saldo - valor

nome = input("Digite seu nome: ")
num = input("Digite o número da conta: ")
x = Conta()
x.titular = nome
x.numero = num
op = int(input("1 - Saldo, 2 - Depósito, 3 - Saque, 0 - Fim: "))
while op != 0:
    if op == 1:
        print("Seu saldo é", x.saldo)
    if op == 2:
        valor = float(input("Qual o valor do depósito? "))
        x.depositar(valor)
    if op == 3:        
        valor = float(input("Qual o valor do saque? "))
        x.sacar(valor)
    op = int(input("1 - Saldo, 2 - Depósito, 3 - Saque, 0 - Fim: "))
