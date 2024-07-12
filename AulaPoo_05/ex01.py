from corrida import Corrida
from triangulo import Triangulo

class UI:
    @staticmethod
    def menu():
        print("1 - Corrida, 2 - Triangulo, 3 - Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.nova_corrida()
            if op == 2: UI.novo_triangulo()
    @staticmethod
    def nova_corrida():
        c = Corrida() 
        distancia = float(input("Informe a distância em metros: "))
        tempo = input("Informe o tempo no formato 'h:m:s': ")
        c.set_distancia(distancia)
        c.set_tempo(tempo)
        print(f"Seu pace é de {c.pace()} minutos/km")
    @staticmethod
    def novo_triangulo():
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        print(f"A base do triângulo é {x.get_base()}")
        print(f"A altura do triângulo é {x.get_altura()}")
        print(f"A área do triângulo é {x.calc_area()}")

UI.main()