class Calculadora:
    def __init__(self, operacao):
        self.operacao = operacao

    def __call__(self, *args):
        if self.operacao == "somar":
            return sum(args)

        if self.operacao == "multiplicar":
            multiplicacao = 1
            for numero in args:
                multiplicacao *= numero
            return multiplicacao
    
        if self.operacao == "divisao":
            divisao = 1
            for i in args:
                if i == args[0]:
                    divisao = i
                else:
                    divisao /= i
            return divisao

        if self.operacao == "subtrair":
            total = 0
            for i in args:
                if i == args[0]:
                    total = i
                else:
                    total -= i
            return total
            
    

calc = Calculadora("somar")

print(calc(2, 3))
print(calc(10, 5))
print(calc(-7, 4))
print(calc(100, 250))