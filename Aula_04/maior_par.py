print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = []
if a % 2 == 0: x.append(a)
if b % 2 == 0: x.append(b)
if c % 2 == 0: x.append(c)
if d % 2 == 0: x.append(d)

if len(x) == 0: print("Nenhum número par foi informado")
else: print(f"O maior número par é {max(x)}")

