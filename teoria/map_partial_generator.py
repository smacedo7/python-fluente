# map = mapear de um dado para outro dado
# funç map: pega uma funçao e um iteravel
# basicamente com ela passo uma funçaao e oq
# quero mudar nela


from functools import partial


def print_iter(iterator):
    print(*list(iterator), sep='\n')


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumenta_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)


# novos_produtos = [
#     {**p, 'preco': aumenta_dez_porcento(p['preco'])}
#     for p in produtos
# ]

def muda_preco_de_produtos(produto):
    return {
        **produto, 'preco': aumenta_dez_porcento(produto['preco'])
    }


novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))

print_iter(produtos)
print()
print_iter(novos_produtos)
print(
    list(
        map(
            lambda produto: produto * 3,
            [1, 2, 3, 4]
        )
    )
)
