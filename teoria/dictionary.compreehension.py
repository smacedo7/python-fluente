produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}
print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),    
]

dicionario = {
    chave: valor
    for chave, valor in lista
}

print(dicionario)

# set compreehension

s1 = {
    valor for valor in range(10)
}
print(s1)
# ou
s2 = {2 ** i for i in range(0, 11)}
print(s2)