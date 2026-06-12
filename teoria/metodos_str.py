frase = 'Olha só, que coisa interessante'
lista_palavras = frase.split()
print(lista_palavras)  # ['Olha', 'só,', 'que', 'coisa', 'interessante']

lista_palavras = frase.split(',')
print(lista_palavras)  # ['Olha só', ' que coisa interessante'], divide
# na virgula

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())

for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip

# frases_unidas = '-'.join('abc')
# print(frases_unidas)  # a-b-c

frases_unidas = '-'.join(lista_palavras)
print(frases_unidas)

cpf = '746.824.890.70'.replace('.', '')
print(cpf)