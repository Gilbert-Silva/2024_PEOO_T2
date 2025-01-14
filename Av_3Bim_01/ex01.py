from datetime import datetime

class Usuario:                    # 5 - classe
    def __init__(self, e, s):     # 5 - init
        self.__email = e          # 5 - atributos
        self.__senha = s          # 5 - get/set
    def get_email(self):
        return self.__email
    def set_email(self, e):
        self.__email = e 
    def get_senha(self):
        return self.__senha
    def set_senha(self, s):
        self.__senha = s

class NascimentoError(Exception):    # 5 - classe e herança
    def __init__(self, data):        # 5 - atributo
        super().__init__()           # 5 - get
        self.__data = data           # 5 - init
    def get_data(self):
        return self.__data

class Aluno(Usuario):                  # 5 - classe e herança
    def __init__(self, e, s, n, ns):   # 5 - atributos
        super().__init__(e, s)         # 5 - init e super
        self.__nome = n                # 5 - get/set
        self.set_nascimento(ns)        # 5 - raise e validação
    def get_nome(self):                # 5 - mês aniversário
        return self.__nome             # 10 - json
    def set_nome(self, n):
        self.__nome = n 
    def get_nascimento(self):
        return self.__nascimento
    def set_nascimento(self, ns):
        self.__nascimento = ns
        if ns > datetime.now(): # data no futuro
            raise NascimentoError(ns) 
    def mes_aniversario(self):
        return self.__nascimento.month               
    def to_json(self):
        dic = {}
        dic["email"] = self.get_email()
        dic["senha"] = self.get_senha()
        dic["nome"] = self.__nome
        dic["nascimento"] = self.__nascimento.strftime("%d/%m/%Y")
        return dic

def main():
    email = input("Informe o e-mail: ")    # 5 - input
    senha = input("Informe e senha: ")     # 5 - Aluno
    nome = input("Informe o nome: ")       # 10 - try excpet
    nasc = datetime.strptime(input("Informe a data de nascimento: "), "%d/%m/%Y")
    try:
        aluno = Aluno(email, senha, nome, nasc)
        print(aluno.get_email())
        print(aluno.get_senha())
        print(aluno.get_nome())
        print(aluno.get_nascimento())
        print(aluno.mes_aniversario())
        print(aluno.to_json())
    except NascimentoError as erro:
        print("Data não pode estar no futuro")
        print(erro.get_data())    

main()
