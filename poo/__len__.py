# len(objeto) é igual a objeto.__len__()
# usar quando o objeto tiver uma colecao ou uma quantidade natural
# carrinho de compras, biblioteca, vetor, playlist, turma
# usa o len sobre o objeto, nao sobre a lista

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.produtos = []
    
    def adicionar(self, produto):
        self.produtos.append(produto)
    
    # def listar_carrinho(self):
    #     return self.produtos
    
    def listar_carrinho(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)

    def remover(self, produto):
        self.produtos.remove(produto)

    def __len__(self):
        return len(self.produtos)  # quando chama o len, vem direto pra ca
    

carrinho = Carrinho()

carrinho.adicionar(Produto("Mouse", 150))
carrinho.adicionar(Produto("Teclado", 250))
carrinho.adicionar(Produto("Monitor", 1200))

print(carrinho.listar_carrinho)  # <bound method Carrinho.listar_carrinho of <__main__.Carrinho object at 0x102754fd0>>
print(len(carrinho))

# chamar len sempre sobre o objeto