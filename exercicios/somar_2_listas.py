from itertools import zip_longest


def soma_lista(l1, l2):
    tamanho_minimo = min(len(l1), len(l2))
    return [
        (l1[i] + l2[i])
        for i in range(tamanho_minimo)
    ]


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
print(soma_lista(lista_a, lista_b))

lista = []
for i, l in enumerate(lista_b):
    lista.append(lista_a[i] + lista_b[i])
print(lista)

soma_lista = []
for i in range(len(lista_b)):
    soma_lista.append(lista_a[i] + lista_b[i])
print(soma_lista)

somaa_lista = [
    x + y
    for x, y in zip_longest(lista_a, lista_b, fillvalue=0)
]
print(somaa_lista)
