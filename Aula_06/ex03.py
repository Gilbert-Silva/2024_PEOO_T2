class Aluno:
    def __init__(self):       # construtor
        self.nome = ""        # atributo
        self.matricula = ""
    def ano_ingresso(self):   # método
        return int(self.matricula[0:4])
    
a = Aluno()
a.nome = "Rafaela"
a.matricula = "20231011110987"
b = Aluno()
b.nome = "Miguel"
b.matricula = "20231011117890"

print(a.nome, a.matricula, a.ano_ingresso())
print(b.nome, b.matricula, b.ano_ingresso())


