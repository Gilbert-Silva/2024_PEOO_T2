import enum

class Pagamento(enum.Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

class Boleto:
    def __init__(self, valor):
        self.valor = valor
        self.situacao_pagamento = Pagamento.EmAberto
    def pagar(self, valor_pago):
        if self.valor == valor_pago:
            self.situacao_pagamento = Pagamento.Pago
        else:
            self.situacao_pagamento = Pagamento.PagoParcial

b = Boleto(1000)
print(b.situacao_pagamento)
b.pagar(100)
print(b.situacao_pagamento)
b.pagar(1000)
print(b.situacao_pagamento.name)



