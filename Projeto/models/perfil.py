# Lista de Clientes
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json

# Modelo
class Perfil:
  def __init__(self, id, nome, descricao, beneficios):
    self.id = id
    self.nome = nome
    self.descricao = descricao
    self.beneficios = beneficios
  def __str__(self):
    return f"{self.nome} - {self.descricao} - {self.beneficios}"

# Persistência
class Perfis:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.id > m: m = c.id
    obj.id = m + 1
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.descricao = obj.descricao
      c.beneficios = obj.beneficios
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    cls.objetos.sort(key=lambda x : x.nome)
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("perfis.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("perfis.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Perfil(obj["id"], obj["nome"], obj["descricao"], obj["beneficios"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

