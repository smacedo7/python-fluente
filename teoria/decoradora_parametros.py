def fabrica_de_decoradores(a=None, b=None, c=None):    
    def fabrica_de_funcoes(func):
        print('decoradora 1')

        def aninhada(*args, **kwargs):
            print('aninhada')
            print('parametros da fabrica: ', a, b, c)
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)  # vira fabrica_de_funcoes que pega soma
def soma(x, y):
    return x + y
# logo soma = aninhada
# msm coisa que soma = fabrica_de_funcoes(soma)

# retorna ate aqui decorada 1,
# se add mais coisas:


# dez_mais_cinco = soma(10, 5)
# print(dez_mais_cinco)
# decoradora 1
# aninhada
# 15

# ou

decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)
dez_vezes_cinco = multiplica(10, 5)
print(dez_vezes_cinco)

somatorio = soma(10, 5)
print(somatorio)