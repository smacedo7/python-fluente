import sys

"""
iterator: so sabe o proximo valor! é o metodo de uma string
classe q tem medo __iter__ e next

iteravel =  qualquer objeto que pode ser percorrido
ou iterado elemento por elemento (como em um laço for)

"""

iterable = ['eu', 'tenho', '__iter__']
# iterator = iterable.__iter__()]
iterator = iter(iterable)
print(next(iterator))  # eu
print(next(iterator))  # tenho

# generator: funçoes q sabem pausar
"""_summary_
    uma função especial que retorna um iterador preguiçoso ,
    permitindo processar grandes conjuntos
    de dados sequencialmente sem carregá-los todos na memória do sistema de
    uma só vez. Em vez de construir e manter uma lista inteira na RAM,
    os geradores usam avaliação preguiçosa para produzir valores sob demanda,
    um de cada vez, resultando em uma economia significativa de memória
"""

lista = [n for n in range(10)]
print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

generator = (n for n in range(10))
print(generator)  # <generator object <genexpr> at 0x000002776F8F8E10>

print(sys.getsizeof(lista))  # 184
print(sys.getsizeof(generator))  # 200

print(next(generator))  # 0
print(next(generator))  # 1
print(next(generator))  # 2

# for n in generator:
#     print(n)  
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8


# def generator(n=0):
#     yield 1  # pausar a funçao
#     # return 'ACABOU'
#     print('continuando')
#     yield 2  # pausar
#     print('mais uma...')
#     yield 3
#     print('vou terminar')
#     # return 'Vou terminar'


# gen = generator(n=0)
# print(next(gen))
# print(next(gen))  # StopIteration: ACABOU
# print(next(gen))
# # print(next(gen))

def generator(n=0, maximun=10):
    while True:
        yield n
        n += 1

        if n >= maximun:
            return


gen = generator(n=0)
for n in gen:
    print(n)

# yield!


def gen1():
    print('COMEÇOU GEN 1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN 1')


def gen2():
    print('COMEÇOU GEN 2')
    yield from gen1()
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN 2')


def gen3():
    print('COMEÇOU GEN 3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN 3')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for numero in g1:
    print(numero)
print()

for numero in g2:
    print(numero)
print()

for numero in g3:
    print(numero)
print()