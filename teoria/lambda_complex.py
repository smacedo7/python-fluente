def executa(funçao, *args):
    return funçao(*args)


def soma(x, y):
    return x + y


print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
    executa(soma, 2, 3))

# lambda significa def,
# nao possui nome e nem parenteses
# lambda paramentros: valor q retorna


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


multiplicaçao = cria_multiplicador(2)
print(multiplicaçao(2))

executa_funçao_lambda = executa(
    lambda m: lambda n: n * m,
    2
)
print(executa_funçao_lambda(2))

print(
    executa(
        lambda *args: sum(args),
        2, 3, 4, 5,
    )
)