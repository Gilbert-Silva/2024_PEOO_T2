class Circulo:
    pass

a = Circulo()
b = Circulo()
c = a
x = 5
y = 5
print(id(a))
print(id(b))
print(id(c))
print(id(x))
print(id(y))
print(type(a))
print(type(b))
print(type(c))
print(type(x))
print(type(y))
print(type(print))
z = print
z("Olá pessoal")


