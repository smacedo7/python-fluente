class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
        # ou return self.ano_atual - self.idade


print()
p1 = Pessoa('Samuel', 19)
print(p1.get_ano_nascimento())
print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1 # muda na classe