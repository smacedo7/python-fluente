class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"


p1 = Pessoa("Samuel", 19)
print(p1) # sem __str__ fica: 
# <__main__.Pessoa object at 0x103306f40>

# com __str__ fica: 
# Samuel (19 anos)
# é um jeito de deixar a chamada do objeto entendivel para o usuario,
# nao para o desenvolvedor
