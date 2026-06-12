# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado

pessoa = {
    'nome': 'Samuel',
    'sobrenome': 'Correia'
}

# print(pessoa.__len__())  # 2

print(len(pessoa))  # 2

print(pessoa.keys())  # dict_keys(['nome', 'sobrenome'])
print(pessoa.values())  # dict_values(['Samuel', 'Correia'])
print(pessoa.items())  # dict_items([('nome', 'Samuel'), ('sobrenome', 'Cor')])

# print(tuple(pessoa.keys()))  # ('nome', 'sobrenome')
# print(list(pessoa.keys()))  # ['nome', 'sobrenome']
# print(list(pessoa.values()))  # ['Samuel', 'Correia']
# print(list(pessoa.items()))  # [('nome', 'Samuel'), ('sobrenome', 'Correia')]

for chave, valor in pessoa.items():
    print(chave, valor)

# pessoa.setdefault('idade', 19)
# print(pessoa['idade'])
# print(pessoa.get('nome', None))

# nome = pessoa.pop('nome')
# print(nome)  # Samuel
# print(pessoa)  # {'sobrenome': 'Correia'}

# ultima_chave = pessoa.popitem()
# print(ultima_chave)  # ('sobrenome', 'Correia')
# print(pessoa)  # {'nome': 'Samuel'}

# pessoa.update({
#     'nome': 'novo valor',
#     'idade': 30
# })
# pessoa.update(nome='novo valor', idade=19)
# tupla = (('nome', 'novo valor'), ('idade', 30))
# pessoa.update(tupla)
# print(pessoa)