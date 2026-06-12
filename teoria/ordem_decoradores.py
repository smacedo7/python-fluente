def parametros_decorador(nome):
    def decorador(func):
        print('entrei no decorador')

        def aninhada(*args, **kwargs):
            print('entrei na aninhada')
            res = func(*args, **kwargs)
            final = f'{res}, {nome}'
            return final
        return aninhada
    return decorador


@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):
    return x + y
# soma = aninhada sem executar


somatorio = soma(6, 7)
print(somatorio)
# entrei no decorador
# entrei no decorador
# entrei no decorador
# entrei no decorador
# entrei no decorador
# entrei na aninhada
# entrei na aninhada
# entrei na aninhada
# entrei na aninhada
# entrei na aninhada
# 13, 1, 2, 3, 4, 5

# se executa de baixo pra cima