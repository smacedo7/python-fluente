# É uma variável usada dentro de uma função, mas
# que foi criada em um escopo externo.
# É uma variável usada dentro de uma função,
#  mas que foi criada em um escopo externo.


# Variável local é uma variável que
# existe apenas dentro da função onde foi criada.

def fora(x):
    a = x  # variavel livre, nao
    # ta dentro da dentro()

    def dentro():
        print(locals())  # {'a': 10}
        # locals é tudo q pode acessar no local
        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())  # 10


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))  # ab
