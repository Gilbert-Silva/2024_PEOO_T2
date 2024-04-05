class Conta:
    def __init__(self):
        self.titular = ""
        self.numero = ""
        self.saldo = 0
    def depositar(self, valor):
        self.saldo = self.saldo + valor
    def sacar(self, valor):    
        self.saldo = self.saldo - valor

a = Conta()
a.titular = "Rafaela"
a.numero = "1234"
print(a.titular, a.numero, a.saldo)
a.depositar(300)
print(a.titular, a.numero, a.saldo)
a.sacar(50)
print(a.titular, a.numero, a.saldo)
int("Teste")
