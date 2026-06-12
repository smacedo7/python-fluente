# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

# import sys

# sys.setrecursionlimit(1004)

# def recursiva(inicio=0, fim=10):
#     # caso recursivo:
#     # contar ate chegar o final:
#     # até 10
#     inicio += 1
#     return recursiva(inicio, fim)
#     # da erro pq da stackoverflow


def recursiva(inicio=0, fim=10):
    # Caso base:
    # Esse para a recursão
    print(inicio, fim)
    if inicio >= fim:
        return fim

    # Caso recursivo:
    # contar até chegar em 10
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())
# print(recursiva(0, 1000))


def factorial(n):
    if n <= 1 or n <= 0:
        return 1
    return n * factorial(n - 1)


print()
print(factorial(5))
print(factorial(3))

# sempre no return chama a funçao de novo
# como se fosse um loop
# return 1 ou return fim = base da recursao
# é quando a funçao para de se chamar
