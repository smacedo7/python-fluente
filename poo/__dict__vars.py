class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
        # ou return self.ano_atual - self.idade


print()
dados = {'nome': 'Samuel', 'idade': 19}
p1 = Pessoa(**dados)
# p1 = Pessoa('Samuel', 19)
# p1.nome = 'EITA'
# del p1.nome
print(p1.__dict__)  # {'nome': 'Samuel', 'idade': 19}
print(vars(p1))  # {'nome': 'Samuel', 'idade': 19}