print("Digite uma frase:")
s = input()
total = 0
for x in s:
    if "0" <= x <= "9": total = total + int(x)
print(total)
    

