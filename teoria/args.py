'''
args - passar argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''


x, y, *resto = 1, 2, 3, 4, 5, 6, 7

# print(x, y, resto)


# def soma(*args):
#     total = 0
#     for numero in args:
#         print(total, numero)
#         total += numero
#         print(total)
#     print(total)

# soma(1, 2, 3, 4, 5, 6)

def soma(*args):
    total = 0
    for numero in args:
        # print(total, numero)
        total += numero
    return total


soma_de_tudo = soma(1, 2, 3, 4, 5, 6)
# print(soma_de_tudo)  # 21

# print(sum(1, 2, 3, 4))  # TypeError: sum() takes at most 2 arguments (4 given)

numeros = 1, 2, 3, 4, 5, 6
print(sum(numeros))  # 21

# outra_soma = soma(1, 2, 3, 4, 5, 6)
# print(outra_soma)  # 21

# outra_soma = soma(numeros)  # erro
# print(outra_soma)

outra_soma = soma(*numeros)
print(outra_soma)  # 21