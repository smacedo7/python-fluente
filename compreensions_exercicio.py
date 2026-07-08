numeros = [3, 8, 12, 5, 20, 15]  #  option seta pra cima

# dictionary = {numero: numero ** 2 for numero in numeros if numero > 10}

dictionary = {
    numero: numero ** 2
    for numero in numeros
    if numero > 10
}
 
print(dictionary)

for indice, valor in dictionary.items():
    print(indice, valor)

# Crie um dicionário onde:
# chave = número
# valor = quadrado do número
# Mas apenas para números maiores que 10.
# Resultado:
# {
#     12: 144,
#     20: 400,
#     15: 225
# }