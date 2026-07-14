# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostra_classe(self):
        print('CLASSE PESSOA')
        print(f'a classe de {self.nome} é {self.__class__.__name__}')


class Aluno(Pessoa):
    def mostra_classe(self):
        print('CLASSE aluno')
        print(f'a classe de {self.nome} é {self.__class__.__name__}')


class Cliente(Pessoa):
    cpf = 'ola pola'


pessoa1 = Pessoa('Samuel melacedo', 19)
pessoa1.mostra_classe()

pessoa2 = Aluno('luiz', 34)
pessoa2.mostra_classe()

pessoa3 = Cliente('pedro augusto', 23)
pessoa3.mostra_classe()  # CLASSE PESSOA -> a classe de pedro augusto é Cliente
print(pessoa3.cpf)