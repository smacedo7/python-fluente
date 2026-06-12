# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest


def zipper(l1, l2):
    # print(min(1, 2))  # 1
    # print(min(150, 200))  # 150
    # print(min(len(l1), len(l2)))  # 3
    intervalo_maximo = min(len(l1), len(l2))
    return [
        (l1[i], l2[i])
        for i in range(intervalo_maximo)
    ]


lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(lista1, lista2))

# ou

print(list(zip(lista1, lista2)))
print(list(zip_longest(lista1, lista2, fillvalue='SEM VALOR')))  # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG'), ('SEM VALOR', 'RJ')]
