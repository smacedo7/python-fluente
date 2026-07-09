class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod  # pertence a classe e nao ao objeto
    def from_string(cls, string):  # queremos que esse metodo crie um objeto
        # e so quem cria objetos é a classe, justamente por isso a chamamos antes
        # da insranciaçao.
        nome, idade = string.split("-")
        return cls(nome, int(idade))

    def __str__(self):
        return f"{self.nome} ({self.idade} ano(s))"

p1 = Pessoa("pedro", 19)
print(p1)
p2 = Pessoa.from_string("samuel melacedo-19")
print(p2)