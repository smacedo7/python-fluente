string = 'samuel'
metodo = 'upper'
"""
dir: ve os metodos disponiveis do objeto
dir(string)

hasattr é pra ver se obejto tem o medo necessario

getattr: usado para acessar ou obter 
dinamicamente o valor de um atributo de um objeto pelo seu nome

"""

# if hasattr(string, 'upper'):
#     print(True, string.upper())

if hasattr(string, 'upper'):
    print(True)
    print(getattr(string, metodo)())
else:
    print('nao existe o metodo', metodo)