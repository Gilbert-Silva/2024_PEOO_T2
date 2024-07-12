class Triangulo:              # Entidade
    def __init__(self):       # construtor
        self.__b = 0          # atributos encapsulado
        self.__h = 0
    def set_base(self, valor):  # armazenar um valor, antes é feita a validação
        if valor >= 0: self.__b = valor
        else: raise ValueError("Valor da base não pode ser negativo")
    def get_base(self):         # retornar um valor
        return self.__b
    def set_altura(self, valor):
        if valor >= 0: self.__h = valor
        else: raise ValueError("Valor da altura não pode ser negativo")
    def get_altura(self):    
        return self.__h
    def calc_area(self):      # métodos = operação - método de instância
        return self.__b * self.__h / 2
