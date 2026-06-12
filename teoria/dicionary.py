# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

# pessoa = {
#     'nome': 'Luis Otávio',
#     'sobrenome': 'Cancelo Joao',
#     'idade': 18,
#     'altura': 1.80,
#     'endereços': [
#         {'rua': 'tal tal', 'numero': 123},
#         {'rua': 'outra rua', 'numero': 321},
#     ],
# }
# print(pessoa)

# print(pessoa['nome'])
# print(pessoa['sobrenome'])

# for chave in pessoa:
#     print(chave, pessoa[chave])

# pessoa2 = {}
# print(pessoa2)  # {}
# pessoa2['nome'] = 'Samuel Macedo'
# print(pessoa2)  # {'nome': 'Samuel Macedo'}

pessoa3 = {}

chave = 'nome'
pessoa3[chave] = 'Samuel '
pessoa3['sobrenome'] = 'Macedo'

print(pessoa3[chave])  # Samuel
pessoa3[chave] = 'Maria'
print(pessoa3[chave])  # Maria

del pessoa3['sobrenome']
print(pessoa3)  # Maria

print(pessoa3.get('sobrenome'))  # None
print(pessoa3.get('nome'))  # Maria


if pessoa3.get('sobrenome') is None:  # None é valor padrao de .get
    print('Chave nao existe')
else:
    print('A chave existe! ')