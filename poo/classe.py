# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

# classe: molde
# instancia: Objeto criado a partir de uma classe.
# atributos = caracteristicas
# metodos = açoes

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


pessoa1 = Pessoa('Samuel', 'Macedo')
# pessoa1.nome = 'Samuel'
# pessoa1.sobrenome = 'Macedo'
# print(pessoa1)

print(pessoa1.nome)
print(pessoa1.sobrenome)