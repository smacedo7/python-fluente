# iteravel = qualquer objeto que pode ser percorrido
# ou iterado elemento por elemento

# Desempacotamento em Python é
# uma técnica que extrai elementos de uma coleção (como listas, tuplas ou
#  dicionários) e os atribui a variáveis individuais em uma única linha,
# facilitando a manipulação dos dados
# cada argumento fica separado, sai da lista ou dicionario


# print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista = [1 for numero in range(10)]  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]#
# print(lista)
lista = [numero for numero in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# print(lista)


# MAPEAMENTO: 
# fazer uma nova lista com dados baseados 
# em uma lista anterior, mantendo seu tamanho


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    elemento for elemento in produtos
]
# print(*novos_produtos, sep='\n')
# {'nome': 'p1', 'preco': 20}
# {'nome': 'p2', 'preco': 10}
# {'nome': 'p3', 'preco': 30}

novos_produtos = [
    {'nome': produto['nome'], 'preco': produto['preco']}
    for produto in produtos
]
# print(*novos_produtos, sep='\n')  # {'nome': 'p1', 'preco': 20}
# {'nome': 'p2', 'preco': 10}
# {'nome': 'p3', 'preco': 30}

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]
# {**produto}

# ele cria uma cópia do dicionário:

# {
#     'nome': 'p3',
#     'preco': 30
# }

print(novos_produtos)

# novos_produtos = [
#     produto
#     for produto in produtos
# ]
# print(novos_produtos)  # [{'nome': 'p1', 'preco': 20},
# {'nome': 'p2', 'preco': 10}, {'nome': 'p3', 'preco': 30}]

print()
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')

# Filtro de dados em list comprehension (filter)

# lista = [n for n in range(10) if n < 5]
# print(lista) # [0, 1, 2, 3, 4]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]

# valor se isso acontecer se nao valor para cada variavel
# em iteravel percorrido se condiçao de valor for realizada

print(novos_produtos) #[{'nome': 'p1', 'preco': 20},
# {'nome': 'p3', 'preco': 31.5}]

lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

# print(lista)
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

print()
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
# print(lista)
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

lista = [
    [x for y in range(3)]
    for x in range(3)
]
# print(lista)
# [[0, 0, 0], [1, 1, 1], [2, 2, 2]]

lista = [
    [letra for letra in 'Samuel']
    for x in range(3)
]
print(lista)