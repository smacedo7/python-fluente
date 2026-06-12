lista = [5, 4, 7, 11, 20, 1, 9, 3]
lista.sort()
print(lista)  # [1, 3, 4, 5, 7, 9, 11, 20]
# sorted(lista)  # copia rasa da lista, shallow copy
lista.sort(reverse=True)
print(lista)  # [20, 11, 9, 7, 5, 4, 3, 1]

lista2 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista2.sort() nao funciona! 


# def ordena(item):
#     return item['sobrenome']


# lista2.sort(key=ordena)
# for item in lista2:
#     print(item)

def exibe(lista):
    for item in lista:
        print(item)


l1 = sorted(lista2, key=lambda item: item['nome'])  # shallow copy
l2 = sorted(lista2, key=lambda item: item['sobrenome'])

exibe(l1)
print()
exibe(l2)


lista2.sort(key=lambda item: item['nome'])
print(lista2)