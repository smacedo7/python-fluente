# Combinations, Permutations e Product - Itertools

# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

# print(*list(combinations(pessoas, 2)), sep='\n')
print_iter(combinations(pessoas, 2))
# ('João', 'Joana')
# ('João', 'Luiz')
# ('João', 'Letícia')
# ('Joana', 'Luiz')
# ('Joana', 'Letícia')
# ('Luiz', 'Letícia')

print()
print_iter(permutations(pessoas, 2))
# ('João', 'Joana')
# ('João', 'Luiz')
# ('João', 'Letícia')
# ('Joana', 'João')
# ('Joana', 'Luiz')
# ('Joana', 'Letícia')
# ('Luiz', 'João')
# ('Luiz', 'Joana')
# ('Luiz', 'Letícia')
# ('Letícia', 'João')
# ('Letícia', 'Joana')
# ('Letícia', 'Luiz')

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

# print()
# print(list(product(camisetas)))
# [(['preta', 'branca'],), (['p', 'm', 'g'],),
#  (['masculino', 'feminino', 'unisex'],), (['algodão', 'poliéster'],)]

print()
print_iter(product(*camisetas))
# ('preta', 'p', 'masculino', 'algodão')
# ('preta', 'p', 'masculino', 'poliéster')
# ('preta', 'p', 'feminino', 'algodão')
# ('preta', 'p', 'feminino', 'poliéster')
# ('preta', 'p', 'unisex', 'algodão')
# ('preta', 'p', 'unisex', 'poliéster')
# ('preta', 'm', 'masculino', 'algodão')
# ('preta', 'm', 'masculino', 'poliéster')
# ('preta', 'm', 'feminino', 'algodão')
# ('preta', 'm', 'feminino', 'poliéster')
# ('preta', 'm', 'unisex', 'algodão')
# ('preta', 'm', 'unisex', 'poliéster')
# ('preta', 'g', 'masculino', 'algodão')
# ('preta', 'g', 'masculino', 'poliéster')
# ('preta', 'g', 'feminino', 'algodão')
# ('preta', 'g', 'feminino', 'poliéster')
# ('preta', 'g', 'unisex', 'algodão')
# ('preta', 'g', 'unisex', 'poliéster')
# ('branca', 'p', 'masculino', 'algodão')
# ('branca', 'p', 'masculino', 'poliéster')
# ('branca', 'p', 'feminino', 'algodão')
# ('branca', 'p', 'feminino', 'poliéster')
# ('branca', 'p', 'unisex', 'algodão')
# ('branca', 'p', 'unisex', 'poliéster')
# ('branca', 'm', 'masculino', 'algodão')
# ('branca', 'm', 'masculino', 'poliéster')
# ('branca', 'm', 'feminino', 'algodão')
# ('branca', 'm', 'feminino', 'poliéster')
# ('branca', 'm', 'unisex', 'algodão')
# ('branca', 'm', 'unisex', 'poliéster')
# ('branca', 'g', 'masculino', 'algodão')
# ('branca', 'g', 'masculino', 'poliéster')
# ('branca', 'g', 'feminino', 'algodão')
# ('branca', 'g', 'feminino', 'poliéster')
# ('branca', 'g', 'unisex', 'algodão')
# ('branca', 'g', 'unisex', 'poliéster')