from dados import produtos
from copy import deepcopy


novos_produtos = [
    {**item, 'preco': round(item['preco'] * 1.10, 2)}
    for item in deepcopy(produtos)
]

ordenados_nome = sorted(
    deepcopy(produtos),
    key=lambda p:
    p['nome'],
    reverse=True
)

ordenados_preco = sorted(
    deepcopy(produtos),
    key=lambda p:
    p['preco']
)

# final
print(*produtos, sep='\n')
print()
print(*ordenados_nome, sep='\n')
print()
print(*ordenados_preco, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()