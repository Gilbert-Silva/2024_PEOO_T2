class Corrida:
    def __init__(self):
        self.distancia = 1  # metros
        self.horas = 0 
        self.minutos = 0
        self.segundos = 1
    def pace(self):
        t = self.horas * 60 + self.minutos + self.segundos / 60
        d = self.distancia / 1000
        return t/d    

c = Corrida()    
c.distancia = float(input("Informe a distância em metros: "))
c.horas = int(input("Informe o tempo em horas: "))
c.minutos = int(input("Informe o tempo em minutos: "))
c.segundos = int(input("Informe o tempo em segundos: "))
print(f"Seu pace é de {c.pace()} minutos/km")

