# Exercício Análise de Números

# Objetivo: Desenvolver um programa que solicita ao usuário a entrada de
# um número e, com base nesse número, realiza as seguintes operações:

#     1. Mostrar o número informado.
#     2. Informar se o número é par ou ímpar.
#     3. Informar se o número é positivo, negativo ou zero.
#     4. Se o número for positivo, calcular e mostrar sua raiz quadrada.

# """

import math

numero = int(input(""))

print(numero)

if numero % 2 == 0:
    print("é par")
else:
    print("é ímpar")

if numero >= 1:
    print('é positivo')
    print('raiz quadrada: ', math.sqrt(numero))

elif numero == 0:
    print('é zero')
else:
    print('é negativo')
