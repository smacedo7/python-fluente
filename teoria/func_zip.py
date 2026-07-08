# func zip é uma função que recebe dois ou mais iteráveis 
# e retorna um iterador de tuplas, onde cada tupla contém 
# elementos correspondentes dos iteráveis fornecidos. 
# A função zip é útil para combinar listas, 
# tuplas ou outros iteráveis em pares ou grupos.

lista1 = ["ana", "joao"]
lista2 = [20, 18]

for nome, idade in zip(lista1, lista2):
    print(nome, idade)
