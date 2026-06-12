class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('hey')

    @classmethod
    def criar_com_50(cls, nome):
        return cls(nome, 50)

    @classmethod
    def sem_nome(cls, idade):
        return cls('anonima', 50)


print()
p1 = Pessoa('Samuel', 19)

Pessoa.metodo_de_classe()  # so funciona com classmethod
# e tem q ter pessoa

p2 = Pessoa.criar_com_50('Jaqueline')
print(p2.nome, p2.idade)

p3 = Pessoa.sem_nome(45)  # Jaqueline 50
print(p3.nome, p3.idade)  # anonima 50

# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.