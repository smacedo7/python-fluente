# passar: funcao, iterator e valor inicial q vai acumular
# se criar funçao: deve ter como parametro acumulador e lista
# e retornar acumulador + lista['preco']

from functools import reduce


produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# total = 0
# for produto in produtos:
#     total += produto['preco']
# print(round(total, 2))

# print(
#     sum([
#         p['preco']
#         for p in produtos
#     ])
# )
# 44


def funcao_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']


total = reduce(
    # lambda acumulador, produto:
    # acumulador + produto['preco'],
    funcao_reduce,
    produtos,
    0
)

print('total é:', total)
# total é: 4
