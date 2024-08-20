x = 1
y = 2.5
z = "Teste"

print(type(x))
print(type(y))
print(type(z))

class Cliente:
    pass

a = Cliente()
b = Cliente()

print(type(a))
print(type(b))

k = []
print(type(k))
k.append(x)
k.append(b)
print(type(k))
print(k)

x = int()
k = list()
a = Cliente()
print(x)
print(k)
print(a)
