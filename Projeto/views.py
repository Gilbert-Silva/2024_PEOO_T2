from models.cliente import Cliente, Clientes

class View:
    def cliente_inserir(nome, email, fone):
        obj = Cliente(0, nome, email, fone)
        Clientes.inserir(obj)
      
    def cliente_listar():
      return Clientes.listar()

    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        Clientes.atualizar(obj)

    def cliente_excluir(id):
        obj = Cliente(id, "", "", "")
        Clientes.excluir(obj)


