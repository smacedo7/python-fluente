import os

# Métodos úteis:
#     append - Adiciona um item ao final
#     insert - Adiciona um item no índice escolhido
#     pop - Remove do final ou do índice escolhido
#     del - apaga um índice
#     clear - limpa a lista
#     extend - estende a lista
#     + - concatena listas

# metodo = é uma função vinculada a um objeto específico, ou seja classe

string = 'salim'
print(string[0])
lista = list()
print(lista)  # []
print(bool(lista))  # false

lista = [123, True, 'Luiz Otávio', 1.2, []]
print(lista)
print(bool(lista))  # true
print(lista[2].upper(), type(lista[2]))  # ----- luiz otavio, str
print(lista[2])  # luiz otavio

lista[-3] = 'maria'
print(lista[-3])  # maria

bando = [10, 20, 30, 40]
numero = bando[2]
print(numero)  # 30

# crud = creat read update delete

bando[2] = 300  # print(bando[2]) = 300
del bando[2]
print(bando)  # printar bando todo, bando[2] sai e o [3] vira o [2]

bando.append(50)
bando.append(60)
bando.append(70)
print(bando)  # [10, 20, 40, 50, 60, 70]

bando.pop()  # ultimo elemento, print(bando)= [10, 20, 40, 50, 60]
ultimo_valor = bando.pop()
print(bando, 'removido: ', ultimo_valor)  # [10, 20, 40, 50] removido:  60
ultimo_valor2 = bando.pop(2)
print(bando, 'removido: ', ultimo_valor2)  # [10, 20, 50] removido:  40
bando.append(123)
del bando[-1]  # para quando nao souber o tamanho da lista

os.system('cls' if os.name == 'nt' else 'clear')
cocozin = [123, 321, 456, 768, 891, 917]
cocozin.clear()
print(cocozin)  # []

print(bando)  # [10, 20, 50]
bando.insert(0, 5)  # .insert leva sempre dois argumentos posicionais
print(bando)  # [5, 10, 20, 50]
bando.insert(5000000, 99)  # ve quual é o ultimo argumento posicional e add

os.system('cls' if os.name == 'nt' else 'clear')
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b  # concatenaçao == juntar
print(lista_c)  # [1, 2, 3, 4, 5, 6]

lista_d = lista_a.extend(lista_b)  # é metodo e muda A

print(lista_d)  # none fez açao mas nao retorna valor, nao adianta jogar
# valor de metodo em variavel sempre vai dar none, altera valor de a so

os.system('cls' if os.name == 'nt' else 'clear')

nome = 'Luis'
# nome[1] = 'D'  DEU ERRO PQ É IMUTAVEL

lista_d = [1, 2, 3]
lista_e = lista_d  # estao apontando para a mesma variavel tipo:
# lista_e = lista_d = [1, 2, 3], ou seja, se alterar em uma altera a outra
# pq a lista é mutavel e se vc iguala muda tudo aponta o msm valor
# se fosse imutavel daria certo se pa, list.copy()

lista_d[0] = 'qualquer coisa '
print(lista_e)

lista_e = list.copy(lista_d)

os.system('cls' if os.name == 'nt' else 'clear')

l_nome = ['Maria', 'Helena', 'Laís']
for item in l_nome:
    print(item)

os.system('cls' if os.name == 'nt' else 'clear')

# for (indice, nome) in enumerate(l_nome):
#     print(indice, nome)

indices = range(len(l_nome))

for indice in indices:
    print(indice, l_nome[indice])