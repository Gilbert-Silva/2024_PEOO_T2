print("Digite três números inteiros separados por espaços")
s = input().split()  # 6 - entrada
x = int(s[0])        # 6 - conversão
y = int(s[1])
z = int(s[2])

# soma dos pares
total = 0                  # 6 - somador 
if x % 2 == 0: total += x  # 6 - teste
if y % 2 == 0: total += y
if z % 2 == 0: total += z
print("Total =", total)    # 6 - resultado

# quantidade de pares
total = 0                  # 6 - somador 
if x % 2 == 0: total += 1  # 6 - teste
if y % 2 == 0: total += 1
if z % 2 == 0: total += 1
print("Total =", total)    # 6 - resultado





