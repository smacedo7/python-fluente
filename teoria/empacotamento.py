lista = ['pedro', 'arthur', 'joao']
nome1, nome2, nome3 = lista
print(nome1)

# lista = ['pedro', 'arthur', 'joao']  daria errado pq tem 4 itens na lista,
# mas 3 nas variaveis so, muitos valores pra desempacotar
# nome1, nome2, nome3 = lista
# print(nome1)

nome1, *resto = ['Maria', 'Helena', 'Gabriela']
print(nome1, resto)  # Maria ['Helena', 'Gabriela']
# asterisco desempacota, resto da lista fica na variavel q esta sendo
# desempacotada

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'python', 'é', 'legal'

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')  # Maria Helena 1 2 3 Eduarda
print(*lista)  # Maria Helena 1 2 3 Eduarda
print(lista)  # ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
print(*string)
print(string)