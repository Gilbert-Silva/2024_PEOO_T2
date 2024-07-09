class Triangulo:              # Entidade
    def __init__(self):       # construtor
        self.__b = 0          # atributos encapsulado
        self.__h = 0
    def set_base(self, valor):  # armazenar um valor, antes é feita a validação
        if valor >= 0: self.__b = valor
        else: raise ValueError("Valor da base não pode ser negativo")
    def get_base(self):         # retornar um valor
        return self.__b
    def set_altura(self, valor):
        if valor >= 0: self.__h = valor
        else: raise ValueError("Valor da altura não pode ser negativo")
    def get_altura(self):    
        return self.__h
    def calc_area(self):      # métodos = operação - método de instância
        return self.__b * self.__h / 2

class UI:                     # Interface com o usuário
    @staticmethod             # prints e inputs nessa classe
    def main():               # operação principal da UI - método de classe
        x = Triangulo()

        # versão sem encapsulamento - acesso direto ao atributo
        # qualquer valor é armazenado
        #x.b = float(input("Informe o valor da base: "))
        #x.h = float(input("Informe o valor da altura: "))
        #print(f"A base do triângulo é {x.b}")
        #print(f"A altura do triângulo é {x.h}")

        # versão com encapsulamento - acesso indireto ao atributo
        # set - para guardar um valor
        # get - para recuperar um valor
        # qdo um set é feito - validação
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        
        print(f"A base do triângulo é {x.get_base()}")
        print(f"A altura do triângulo é {x.get_altura()}")

        print(f"A área do triângulo é {x.calc_area()}")

UI.main()                     # rodar o programa       