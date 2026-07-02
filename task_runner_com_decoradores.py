tarefas = {}


def registrar(nome):

    def decorador(func):
        tarefas[nome] = func
        return func

    return decorador


def executa(nome):
    return nome(tarefas[nome])


@registrar("somar")
def somar(*args):
    return sum(args)


# def repetir(vezes):

#     def decorador(func):

#         def interna():

#             for _ in range(vezes):
#                 func()

#         return interna

#     return decorador


# @repetir(3)
# def oi():
#     print('Oi')