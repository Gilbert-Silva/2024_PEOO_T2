from datetime import datetime

class Paciente:
    def __init__(self, nome, nasc):
        if nome == "": raise ValueError("Informe um nome")
        if nasc > datetime.now(): raise ValueError("Informe uma data no passado")
        self.__nome = nome
        self.__nascimento = nasc
    def idade(self):
        hoje = datetime.now()
        tempo = hoje - self.__nascimento  # timedelta - tempo de vida
        dias = tempo.days                 # dias do tempo de vida
        anos = dias // 365
        resto = dias % 365
        meses = resto // 30
        return f"{anos} ano(s), {meses} mes(es)"
    def __str__(self):
        return f"{self.__nome} - {self.__nascimento.strftime('%d/%m/%Y')}"
    
nome = input("Informe seu nome: ")
nasc = input("Informe sua data de nascimento: ")

x = Paciente(nome, datetime.strptime(nasc, "%d/%m/%Y"))
print(x)
print(x.idade())



