class Carrinho:
    def __init__(self):
        self.produtos= []

    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
    
    def remover_produto(self, produto):
        if produto in self.produtos:    
            self.produtos.remove(produto)

    def listar(self):
        for produto in self.produtos:
            print(f"{produto.nome} - R${produto.preco:.2f}")  # eu posso acessar atributos 
            # de outras classes estando nessa classe
        return self.produtos  # inutil pq nao tem como listar objetos
        # so seus atributos, por isso percorrer com laço for

    def total(self):
        return sum(produto.preco for produto in self.produtos)




class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __repr__(self):
        return f"Produto: {self.nome} - Preço {self.preco}"
    


p1 = Produto("Mouse", 150)
p2 = Produto("Teclado", 250)
p3 = Produto("Monitor", 1200)


carrinho = Carrinho()

carrinho.adicionar_produtos(p1)
carrinho.adicionar_produtos(p2)
carrinho.adicionar_produtos(p3)

carrinho.listar()

print(carrinho.total())
print([p1, p2])
# [
#     <Produto object at 0x10f2a4>,
#     <Produto object at 0x10f2b8>,
#     <Produto object at 0x10f2d0>
# ]
# como o python ve a lista de objetos, por isso nao 
# tem como listar-la