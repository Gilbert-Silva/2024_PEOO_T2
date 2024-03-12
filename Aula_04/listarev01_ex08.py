print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a==b or a==c or a==d or b==c or b==d or c==d:
    print("Existem números repetidos")
else:
    maior = max(a, b, c, d)
    menor = min(a, b, c, d)
    print(f"Maior valor = {maior}")
    print(f"Menor valor = {menor}")
    #x = []
    #x.append(a)
    #x.append(b)
    #x.append(c)
    #x.append(d)
    x = [a, b, c, d]
    x.remove(maior)
    x.remove(menor)
    print(f"Soma = {x[0] +  x[1]}")
    t = a + b + c + d - maior - menor
    print(f"Soma = {t}")



