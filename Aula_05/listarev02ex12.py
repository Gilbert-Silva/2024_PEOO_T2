print("Digite dois valores inteiros separados por um operador +, -, * ou /")
s = input()
lista = s.split("+") # tentativa de separar com o operador +
if len(lista) == 2:
    a = int(lista[0])
    b = int(lista[1])
    print(a + b)
lista = s.split("-") # tentativa de separar com o operador -
if len(lista) == 2:
    a = int(lista[0])
    b = int(lista[1])
    print(a - b)
lista = s.split("*") # tentativa de separar com o operador *
if len(lista) == 2:
    a = int(lista[0])
    b = int(lista[1])
    print(a * b)
lista = s.split("/") # tentativa de separar com o operador /
if len(lista) == 2:
    a = int(lista[0])
    b = int(lista[1])
    print(a / b)

