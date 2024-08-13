import enum

class Estacao(enum.Enum):
    Outono = 1
    Inverno = 2
    Primavera = 3
    Verão = 4

class Dia(enum.IntFlag):
    Domingo = 1    # 0000.0001                  0000.0001
    Segunda = 2    # 0000.0010                  0000.0010
    Terça = 4      # 0000.0100    0000.0100     0000.0011
    Quarta = 8     # 0000.1000    0010.0000
    Quinta = 16    # 0001.0000    0010.0100
    Sexta = 32     # 0010.0000
    Sábado = 64    # 0100.0000
    
a = Estacao.Outono
print(a, type(a))

d = Dia(0)
print(d)
d = Dia.Terça
print(d)
d = Dia.Terça | Dia.Sexta
print(d, type(d))

