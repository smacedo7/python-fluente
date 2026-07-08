# primeira resoluç

def registrar(*args, **kwargs):
    dictionary = {
        "args": args,
        "kwargs": kwargs
    }
    return dictionary


lista = [1, 2, 3]
dados = {"cidade": "Brasília", "estado": "Distrito Federal"}
print(registrar(*lista, **dados))

# registrar(10, 20, 30, nome="Samuel", idade=19)
# {
#     "args": (10, 20, 30),
#     "kwargs": {
#         "nome": "Samuel",
#         "idade": 19
#     }
# }

# resolução acertada:

def registrar2(*args, **kwargs):
    return {
        "args": args,
        "kwargs": kwargs
    }

lista2 = [1, 2, 3]
dados2 = {"cidade": "Brasília", "estado": "Distrito Federal"}
print(registrar2(*lista2, **dados2))  # a gente desempacotou aqui a lista2
# ficou tipo registrar2(1, 2, 3, {"cidade": "brasilia", ...})
