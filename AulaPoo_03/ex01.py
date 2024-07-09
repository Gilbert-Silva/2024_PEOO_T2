class Triangulo:
    def __init__(self):    # método especial
        self.b = 0         # atributo ou campo
        self.h = 0
    def calc_area(self):   # método
        return self.b * self.h / 2

x = Triangulo()
x.b = -10
x.h = 20

y = Triangulo()
y.b = float(input("Informe o valor da base: "))
y.h = float(input("Informe o valor da altura: "))

z = Triangulo()

print(x, x.b, x.h, x.calc_area())
print(y, y.b, y.h, y.calc_area())
print(z, z.b, z.h, z.calc_area())
