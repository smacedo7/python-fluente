class Carrinho:
    def __init__(self):
        self._produtos = []

    def inserir_produto(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def soma(self):
        return sum([produto.preço for produto in self._produtos])

    def listar(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preço)
        print()


class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço


p1, p2 = Produto('escova de dente', 3.50), Produto('cacho de uva', 8.33)
carrinho = Carrinho()
carrinho.inserir_produto(p1, p2)
print(carrinho.listar())
print(carrinho.soma())

# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).