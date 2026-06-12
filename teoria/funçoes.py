"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
 argumentos posicionais são aqueles passados para uma função
 com base na sua ordem ou posição

 def saudar(nome, cargo):
    print(f"Olá, {nome}! Você é o nosso novo {cargo}.")

# Chamada com argumentos posicionais:
saudar("Ana", "Engenheira")  # Saída: Olá, Ana! Você é o nosso novo Engenheira.

Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.

"""


def Print(a, b, c):  # parametros
    print('varias 1')


Print(1, 2, 3)  # argumentos q entram nos parametros


# def saudaçao(nome):
#     print(f'Olá {nome}! ')

# saudaçao('joao')

def saudaçao(nome='Sem nome'):  # Olá Sem nome!
    print(f'Olá {nome}! ')


saudaçao()

# funçoes em python retornam none por padrao, se printar no
# pelo vai retornar none


# def soma(x, y):
#     print(f'{x=} {y=}', '|', 'x + y = ', x + y)  # x=1 y=2 | x + y 3


# soma(1, 2)
# soma(y=2, x=1)  # argumento nomeado

def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)  # x=1 y=2 z=5 | x + y + z =  8


soma(1, y=2, z=5)  # se eu nomear um, todos depois dele devem ser
# nomeados!


# def soma2(x, y, z=0):
#     if z:
#         print(f'{x=} {y=} {z=} =', x + y + z)
#     else:
#         print(f'{x=} {y=} =', x + y)


# soma2(1, 2)  # print(f'{x=} {y=} {z=} =', x + y + z)

"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""


def soma2(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} =', x + y + z)
    else:
        print(f'{x=} {y=} =', x + y)


soma2(3, 5)  # x=4 y=5 z=6 = 15
soma2(4, 5, 6)  # x=4 y=5 z=6 = 15

