class Viagem:
    def __init__(self, destino, distancia, litros):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_litros(litros)
    def __str__(self):
        return f"{self.__destino} - {self.__distancia} - {self.__litros}"    
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    def set_destino(self, destino):
        if destino != "": self.__destino = destino
        else: raise ValueError("Destino não pode ser vazio")
    def set_distancia(self, distancia):
        if distancia > 0: self.__distancia = distancia
        else: raise ValueError("Distância não pode ser negativa")  
    def set_litros(self, litros):
        if litros > 0: self.__litros = litros
        else: raise ValueError("Litros não pode ser negativo")  
    def consumo(self):
        return self.__distancia / self.__litros

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
        destino = input("Informe o nome do destino: ") 
        distancia = float(input("Informe a distância até o destino: "))
        litros = float(input("Informe a quantidade de litros de combustível: "))
        v = Viagem(destino, distancia, litros)
        #v.set_destino(destino)
        #v.set_distancia(distancia)
        #v.set_litros(litros)
        print(v)
        #print(f"{v.get_destino()} - {v.get_distancia()} - {v.get_litros()}")      
        print(f"{v.consumo()}")      

UI.main()

