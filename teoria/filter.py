# filtar coisas so q com funçao do python
# passo funçao e iterator como parametro


def filtra_bebecito(lista):
    return lista['preco'] > 100


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = filter(
    # lambda produto: produto['preco'] > 100,
    filtra_bebecito,
    produtos
)
print_iter(novos_produtos)
