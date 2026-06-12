import os

nomes = ['pedro', 'arthur', 'joao']

nomes_enumerados = enumerate(nomes)
print(nomes_enumerados)  # <enumerate object at 0x0000015CC8169530>
print(next(nomes_enumerados))  # (0, 'pedro')

for item in nomes_enumerados:
    print(item)
    # (0, 'pedro')
    # (1, 'arthur')
    # (2, 'joao')

for item in enumerate(nomes):
    print(item)


os.system('cls' if os.name == 'nt' else 'clear')

for item in enumerate(nomes):
    print(item)
# (0, 'pedro')
# (1, 'arthur')
# (2, 'joao')

lista_enumerada2 = list(enumerate(nomes))
print(lista_enumerada2)

for item in enumerate(nomes):
    item_a, item_b = item
    print(item_a, item_b)
    # 0 pedro
    # 1 arthur
    # 2 joao

os.system('cls' if os.name == 'nt' else 'clear')
for indice, valor in enumerate(nomes):
    print(indice, valor)

os.system('cls' if os.name == 'nt' else 'clear')
for tupla_enumerada in enumerate(nomes):
    for items in tupla_enumerada:
        print(items)