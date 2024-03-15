print("Digite dois valores inteiros")
a = int(input())
b = int(input())
# solução 1 - usando max
if a == b: print("Números são iguais")
else: print("Maior =", max(a, b))
# solução 2 - sem max
if a == b: print("Números são iguais")
else: 
    if a > b: print("Maior =", a)
    else: print("Maior =", b)

