class Pais:
    def __init__(self, nome : str, populacao : int, area : float):                      
        if nome == "": raise ValueError("Nome não pode ser vazio")
        if populacao <= 0: raise ValueError("População não pode ser negativa")  
        if area < 0: raise ValueError("Área não pode ser negativa") 
        self.__nome = nome             
        self.__populacao = populacao                 
        self.__area = area
    def __str__(self):  # ToString
        return f"{self.__nome} - {self.__populacao} - {self.__area}"    
    def get_nome(self):                      
        return self.__nome                  
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
        nome = input("Informe o nome do país: ") 
        populacao = int(input("Informe a população do país: "))
        area = float(input("Informe a área do país: "))
        p = Pais(nome, populacao, area)
        #p.set_nome(nome)
        #p.set_populacao(populacao)
        #p.set_area(area)
        print(p)
        print(f"{p.get_nome()} - {p.get_populacao()} - {p.get_area()}")      
        print(f"{p.densidade()}")      

UI.main()

