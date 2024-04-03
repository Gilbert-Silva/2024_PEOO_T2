print("Digite uma frase")
s = input()
for x in range(len(s)):
    if x % 2 == 0: print(s[x], end="")


""" Solução sem usar índice
k = -1
for x in s:
    if k == 1: print(x, end="")
    k = -k

    #Infoweb
    #0123456
"""

