class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome


p1 = Pessoa('samuel')
print(p1.get_nome())  # samuel
print(p1.nome)


class Pessoa2:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome


p1 = Pessoa2('sanji')
print(p1.nome)
print(p1._nome)
