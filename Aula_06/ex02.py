n = []
m = []
for k in range(3):
    nome = input("Informe seu nome: ")
    matr = input("Informe sua matrícula: ")
    n.append(nome)
    m.append(matr)
for k in range(3):
    matr = m[k]
    ano = int(matr[0:4])  # ano = int(m[k][0:4]) 
    print(f"Nome = {n[k]} - Matrícula = {m[k]} - Ano = {ano}")
    

