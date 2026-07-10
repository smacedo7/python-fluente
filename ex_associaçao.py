class Professor:
    lista_alunos = []

    def __init__(self, nome):
        self.nome = nome
    
    def adicionar_aluno(self, name):
        self.lista_alunos.append(name)
    
    def listar_alunos(self):
         print(self.lista_alunos)


class Aluno:
    def __init__(self, nome):
        self.nome = nome


prof = Professor("girafales")
a1 = Aluno("Samuel melacedo")
a2 = Aluno("Ana luiza bressan")

# prof.adicionar_aluno(a1)
prof.adicionar_aluno(a1.nome)
# prof.adicionar_aluno(a2)
prof.adicionar_aluno(a2.nome)
prof.listar_alunos()
print(prof.lista_alunos)
print(Professor.lista_alunos)