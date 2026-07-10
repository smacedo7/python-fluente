# class Pagamento:
#     def __init__(self):
#         pass

#     def pagar(self):
#         return f"{self.__class__.__name__}: \"Pagamento realizado via {self.__class__.__name__}\""

# class Pix(Pagamento):
#     def __init__(self):
#         super().__init__()


# class Cartao(Pagamento):
#     def __init__(self):
#         super().__init__()


# class Boleto(Pagamento):
#     def __init__(self):
#         super().__init__()
    


# def realizar_pagamento(pagamento):
#     if isinstance(pagamento, Pagamento):  # recebe um objeto e verifica se é instancia da classe
#         print(pagamento.pagar())
class Pagamento:
    def __init__(self):
        pass


class Pix(Pagamento):
    def __init__(self):
        super().__init__()

    def pagar(self):
        return "Pix: \"Pagamento realizado via Pix\""

class Cartao(Pagamento):
    def __init__(self):
        super().__init__()

    def pagar(self):
        return "Cartao: \"Pagamento realizado via Cartao\""

class Boleto(Pagamento):
    def __init__(self):
        super().__init__()

    def pagar(self):
        return "Boleto: \"Pagamento realizado via Boleto\""


# def realizar_pagamento(pagamento):
#     if isinstance(pagamento, Pagamento):  # recebe um objeto e verifica se é instancia da classe
#         print(pagamento.pagar())  # nao preciso disso, deixa o proprio python validar

def realizar_pagamento(pagamento):
    print(pagamento.pagar())


pix = Pix()
cartao = Cartao()
boleto = Boleto()

realizar_pagamento(pix)
realizar_pagamento(cartao)
realizar_pagamento(boleto)