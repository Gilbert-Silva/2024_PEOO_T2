from datetime import datetime

class Pessoa:                    # 5 - classe
    def __init__(self, n, ns):   # 5 - init
        self.__nome = n          # 5 - atributos
        self.__nascimento = ns   # 5 - get/set
    def get_nome(self):          # 10 - mês aniversário
        return self.__nome
    def set_nome(self, n):
        self.__nome = n 
    def get_nascimento(self):
        return self.__nascimento
    def set_nascimento(self, ns):
        self.__nascimento = ns
    def mes_aniversario(self):
        return self.__nascimento.month 
    
class SalarioError(Exception):   # 5 - classe e herança
    def __init__(self, s):       # 5 - atributo
        super().__init__()       # 5 - get
        self.__salario = s       # 5 - init
    def get_salario(self):
        return self.__salario

class Funcionario(Pessoa):             # 5 - classe e herança
    def __init__(self, n, ns, m, s):   # 5 - atributos, get/set
        super().__init__(n, ns)        # 5 - init e super
        self.__matricula = n           # 5 - raise e validação
        self.set_salario(s)            # 10 - json
    def get_matricula(self):               
        return self.__matricula             
    def set_matricula(self, m):
        self.__matricula = m 
    def get_salario(self):
        return self.__salario
    def set_salario(self, s):
        self.__salario = s
        if s < 0: 
            raise SalarioError(s) 
    def to_json(self):
        dic = {}
        dic["nome"] = self.get_nome()
        dic["nascimento"] = self.get_nascimento().strftime("%d/%m/%Y")
        dic["matricula"] = self.__matricula
        dic["salario"] = self.__salario
        return dic

def main():
    nome = input("Informe o nome: ")              # 10 - try excpet
    nasc = datetime.strptime(input("Informe a data de nascimento: "), "%d/%m/%Y")
    mat = input("Informe a matricula: ")          # 5 - input
    sal = float(input("Informe o salário: "))     # 5 - Aluno
    try:
        func = Funcionario(nome, nasc, mat, sal)
        print(func.get_nome())
        print(func.get_nascimento())
        print(func.get_matricula())
        print(func.get_salario())
        print(func.mes_aniversario())
        print(func.to_json())
    except SalarioError as erro:
        print("Salário não pode ser negativo")
        print(erro.get_salario())    

main()
