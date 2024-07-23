class Pais:
    def __init__(self):                      # atributos - 10
        self.__nome = "Sem nome"             # encapsulamento - 10
        self.__populacao = 1                 # validação - 10
        self.__area = 1                      # get - 10
    def get_nome(self):                      # set - 10
        return self.__nome                   # cálculo - 10
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def set_nome(self, nome):
        if nome != "": self.__nome = nome
        else: raise ValueError("Nome não pode ser vazio")
    def set_populacao(self, populacao):
        if populacao > 0: self.__populacao = populacao
        else: raise ValueError("População não pode ser negativa")
    def set_area(self, area):
        if area > 0: self.__area = area
        else: raise ValueError("Área não pode ser negativa")
    def densidade(self):
        return self.__populacao / self.__area


class UI:                                              # classe/static - 10
    @staticmethod                                      # menu/main - 10
    def menu():                                        # calcular/obj
        print("1 - Calcular, 2 - Fim")                 # entrada/saída de dados
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: UI.calculo()
    @staticmethod
    def calculo():
        p = Pais()
        nome = input("Informe o nome do país: ") 
        populacao = int(input("Informe a população do país: "))
        area = float(input("Informe a área do país: "))
        p.set_nome(nome)
        p.set_populacao(populacao)
        p.set_area(area)
        print(f"{p.get_nome()} - {p.get_populacao()} - {p.get_area()}")      
        print(f"{p.densidade()}")      

UI.main()

