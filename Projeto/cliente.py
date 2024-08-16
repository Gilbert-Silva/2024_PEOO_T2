# CRUD de clientes - cadastro de clientes - lista
# C - Create - insere um cliente no cadastro
# R - Read - lê os clientes cadastrados
# U - Update - atualiza os dados de um cliente
# D - Delete - remove um cliente do cadastro
import json

class Cliente:
  def __init__(self, id, nome, email, fone):
    self.id = id
    self.nome = nome
    self.email = email
    self.fone = fone
  def __str__(self):
    return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class Clientes:
  objetos = []  # atributo estático
  @classmethod
  def inserir(cls, obj):
    cls.objetos.append(obj)
  @classmethod
  def listar(cls):
    return cls.objetos
  @classmethod
  def salvar(cls):  
    with open("clientes.json", mode = "w") as arquivo:   # write
        json.dump(cls.objetos, arquivo, default = vars) 
  @classmethod
  def abrir(cls):
    cls.objetos = []
    with open("clientes.json", mode = "r") as arquivo:   # read
      texto = json.load(arquivo)
      for obj in texto:
        c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])                     # dicionário
        cls.objetos.append(c)

      
#a = Cliente(1, "Douglas Crockford", "d@email.com", "1234")  # json
#b = Cliente(2, "Jon Bosak", "j@email.com", 4321)          # xml
#crud = Clientes()
#crud.inserir(a)
#crud.inserir(b)
Clientes.abrir()
for c in Clientes.listar(): print(c)
#crud.salvar()






  
