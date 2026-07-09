class Produto:
    def __init__(self, preco):
        self.preco = preco  # isso aqui chama o setter automaticamente!
        # estrutura setter = objeto.preco = valor, entao no proprio init ja chama ele
        # assim que eu enviar um valor aqui na instanciaçao, 
        # ja vai pro setter! mesmo que eu nao tenha chamado o setter ainda no p1.preco = valor
        # por exemplo se p1 = Produto(2.99), nao vai direto pra self._preco = 10,
        # pq ele viu que precisa de um setter e ele vai pra validaçao dele.
        # na pratica é como se executasse self.preco(2.99)
        # setter chamado, valida o valor e entao: self._preco = preco

    # porteiro para ler valor, o python faz Produto.preco()
    @property
    def preco(self):
        return self._preco  # retorna metodo protegido pra nao entrar num loop

    # porteiro para alterar valor
    @preco.setter
    def preco(self, preco):
        if preco < 0:
            raise ValueError("Valor inválido")
        self._preco = preco  # retorna metodo protegido pra nao entrar num loop


bolacha = Produto()
print(bolacha)  # <__main__.Produto object at 0x1094ebfd0>

print(bolacha.preco)  # None

bolacha.preco = 2.50
print(bolacha.preco)  # 2.50

bolacha.preco = -1  # raise error aqui 
print(bolacha.preco)

# Getter e Setter não existem para pegar e colocar valores. 
# Eles existem para interceptar a leitura e a escrita de um atributo.