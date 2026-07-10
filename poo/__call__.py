# permite chamar objeto como func
# objeto(...)
# objeto.__call__(...)
# usar quando um objeto representa uma operacao configurada
# calculadora, validador, filtro, processador

class Calculadora:
    def __init__(self, operacao):
        self.operacao = operacao
    
    def __call__(self, a, b):
        if self.operacao == "somar":
            return a + b
        elif self.operacao == "subtrair":
            return a - b
        elif self.operacao == "multiplicar":
            return a * b
        else:
            if b == 0:
                raise ZeroDivisionError("Dividiou por zero otario burro")
            return a / b


somador = Calculadora("somar")
multiplicador = Calculadora("multiplicar")
print(somador(4, 5))  # lembra closure se pa, mentira nao retorna func interna mas
print(multiplicador(6, 7))  # serve literalmente como uma func

# call tranforma objeto numa func