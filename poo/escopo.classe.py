class Animal:
    # nome = 'leao'
    def __init__(self, nome):
        self.nome = nome

    def acao(self):
        return f'{self.nome} esta executando uma açao'

    def comendo(self, comida):
        return f'{self.nome} esta comendo {comida}'

    def executando(self, *args, **kwargs):
        return f'{self.nome} está {self.comendo(*args, **kwargs)}'


print()
# print(Animal.nome)  # leao
leao = Animal('leao')
print(leao.nome)
print(leao.acao())
print(leao.comendo('cibola'))  # leao esta comendo cibola
print(leao.executando('cibolitos'))  # leao está leao esta comendo cibolitos
