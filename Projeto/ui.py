from models.horario import Horario, Horarios
from datetime import datetime
from views import View

#Visão
class UI:
  @staticmethod
  def menu():
    print("Cadastro de Clientes")
    print("  1 - Inserir, 2 - listar, 3 - atualizar, 4 - excluir")
    print("Cadastro de Horários")
    print("  5 - Inserir, 6 - listar, 7 - atualizar, 8 - excluir")
    print("Outras opções")
    print("  9 - Fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 9: 
      op = UI.menu()
      if op == 1: UI.cliente_inserir()
      if op == 2: UI.cliente_listar()
      if op == 3: UI.cliente_atualizar()
      if op == 4: UI.cliente_excluir()
      if op == 5: UI.horario_inserir()
      if op == 6: UI.horario_listar()
      if op == 7: UI.horario_atualizar()
      if op == 8: UI.horario_excluir()

  @staticmethod
  def cliente_inserir():
    nome = input("Informe o nome: ")
    email = input("Informe o e-mail: ")
    fone = input("Informe o fone: ")
    View.cliente_inserir(nome, email, fone)
    #c = Cliente(0, nome, email, fone)
    #Clientes.inserir(c)

  @staticmethod
  def horario_inserir():
    datastr = input("Informe a data e o horário no formato dd/mm/aaaa hh:mm: ")
    data = datetime.strptime(datastr, "%d/%m/%Y %H:%M")
    c = Horario(0, data)
    Horarios.inserir(c)

  @staticmethod
  def cliente_listar():
    for c in View.cliente_listar(): print(c)
    #for c in Clientes.listar(): print(c)

  @staticmethod
  def horario_listar():
    for c in Horarios.listar():
      print(c)

  @staticmethod
  def cliente_atualizar():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    email = input("Informe o novo e-mail: ")
    fone = input("Informe o novo fone: ")
    View.cliente_atualizar(id, nome, email, fone)
    #c = Cliente(id, nome, email, fone)
    #Clientes.atualizar(c)

  @staticmethod
  def horario_atualizar():
    pass

  @staticmethod
  def cliente_excluir():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    View.cliente_excluir(id)
    #c = Cliente(id, "", "", "")
    #Clientes.excluir(c)

  @staticmethod
  def horario_excluir():
    pass
  
UI.main()    





  
