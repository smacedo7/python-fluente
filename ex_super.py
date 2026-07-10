class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina


a1 = Aluno("Samuel", 19, "202612345")
p1 = Professor("Carlos", 45, "POO")

print(a1.nome)
print(a1.idade)
print(a1.matricula)

print()

print(p1.nome)
print(p1.idade)
print(p1.disciplina)

# quando na classe filha tiver init, tomar cuidado
# usar super, pq ai inicializa da classe mae
# primeiro procura na classe filha depois passa pra mae 
# e assim por adiante 
# se a filha tiver init, ele nao procura na classe mae