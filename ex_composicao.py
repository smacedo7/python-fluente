class Casa:
    def __init__(self, endereco):  # nao preciso solicitar lista de comodos aqui afinal é um parametro
        # posso criar atributos que nao estao solicitados neles
        self.endereco = endereco
        self.lista_de_comodos = []
    
    def adicionar_comodo(self, nome):
        self.lista_de_comodos.append(Comodo(nome))  # nao coloquei um objeto em uma variavel, por isso é composicao
    
    def listar_comodos(self):
        for comodo in self.lista_de_comodos:  # como eu so adicionei o objeto, preciso saber seu nome
            print(comodo.nome, end=' ')

class Comodo:
    def __init__(self, nome):
        self.nome = nome

casa = Casa("Rua das Flores")

casa.adicionar_comodo("Sala")
casa.adicionar_comodo("Quarto")
casa.adicionar_comodo("Banheiro")

casa.listar_comodos()

