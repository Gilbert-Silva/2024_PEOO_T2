print("Digite uma frase:")
s = input()

palavras = s.split()
for x in range(len(palavras)):
    print(*palavras)
    palavras.remove(palavras[0])
    
