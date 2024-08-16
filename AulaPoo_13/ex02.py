import json

class Cliente:
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome
  def __str__(self):
    return f"{self.id} - {self.nome}"

def salvar():  
  a = Cliente(1, "Douglas Crockford")  # json
  b = Cliente(2, "Jon Bosak")          # xml
  lista = [a, b]
  #print(a)
  #print(b)
  #print(a.__dict__)
  #print(vars(b))  # serialização
  with open("clientes.json", mode = "w") as arquivo:   # write
    json.dump(lista, arquivo, default = vars)

def abrir():
  lista = [] 
  with open("clientes.json", mode = "r") as arquivo:   # read
    texto = json.load(arquivo)
    for obj in texto:
      c = Cliente(obj["id"], obj["nome"])                     # dicionário
      lista.append(c)
  for c in lista: print(c)

#salvar()
abrir()





