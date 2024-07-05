class Aluno:
    def __init__(self):
        self.nome = ""
        self.matricula = ""
        self.email = ""
    def ano_ingresso(self):
        return self.matricula[0:4]
    def curso(self):
        return self.matricula[5:10]

a1 = Aluno()
a1.nome = "Renato"
a1.matricula = "20231011111234"
a1.email = "renato@ifrn.edu.br"
print(a1.nome, a1.matricula, a1.email, a1.ano_ingresso(), a1.curso())

a2 = Aluno()
a2.nome = "Rafaela"
a2.matricula = "20231011119876"
a2.email = "rafaela@ifrn.edu.br"
print(a2.nome, a2.matricula, a2.email, a2.ano_ingresso(), a2.curso())        