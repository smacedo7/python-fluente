# kwargs = argumentos nomeados
# argumento nomeados sao os parametros da funcao
# com valores definidos
# exemplo> chama(slime='bosta')
# kwargs - keyword arguments (argumentos nomeados)

a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

pessoa2 = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa2 = {
    'idade': 16,
    'altura': 1.6,
}
pessoas_completo = {**pessoa2, **dados_pessoa2}
print(pessoas_completo)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('nao nomeados = ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(nome='joana', qlq=123)  # nome joana
# qlq 123
mostro_argumentos_nomeados(**configuracoes)
# arg1 1
# arg2 2
# arg3 3
# arg4 4