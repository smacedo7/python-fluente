class Calculadora:
    
    # staticmethod afirma que a func 
    # pertence a classe apenas por organizaçao
    # e para nao passar self nem cls automaticamente
    @staticmethod  
    def somar(a, b):
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ZeroDivisionError("dividiu por zero seu burro")
        return a / b


numero = Calculadora()
print(numero.somar(4, 5))
print(Calculadora.somar(5, 3))
print(Calculadora.subtrair(5, 3))
print(Calculadora.multiplicar(5, 3))
print(Calculadora.dividir(6, 2))