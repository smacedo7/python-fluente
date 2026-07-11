"""
executado antes do dunder init,
cria e retorna o objeto quando:

usuario = Usuario("Samuel")

o python faz:

objeto = Usuario.__new__(Usuario, "Samuel")

nao passa self pq aind nao tem a instancia, afinal ta criando agora

depois

Usuario.__init__(objeto, "Samuel")
recebe cls pq ainda nao tem uma instancia para ser colocada no self

new -> cria o onjeto -> init -> configura o objeto

diferença entre new e init:

new -> cria o objeto e retorn o objeto
init -> recebe o objeto ja criado, apenas configura seus atributos e sempre retorna none

usar quando precisar controlar a criaçao do objeto antes dele existir.

deve sempre retornar o novo objeto
"""

class Pessoa:

    def __new__(cls, objeto):
        print("Criando objeto...")
        print(f"{objeto}")
        return super().__new__(cls)

    def __init__(self, nome):
        print("inicializando objeto...")
        self.nome = nome

p = Pessoa("samuel")






# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):  # chamado antes do init
        # responsavel por criar classe
        print("criando o objeto")
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, x):
        print("inicializando o objeto")
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)

# O que é new?

# É o método responsável por CRIAR o objeto.

# Ele é chamado antes do __init__.

# No __new__ não existe self ainda.

# Porque o objeto nem foi criado.

# Deve retornar:

# super().__new__(cls)

# ou algum objeto.