# Fatorial de um número
#5! = 1 x 2 x 3 x 4 x 5
x = int(input("Informe um número para o cálculo do fatorial: "))
p = 1
for k in range(1, x + 1):
    p *= k
print(p)


