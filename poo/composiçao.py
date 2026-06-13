# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def __del__(self):
        print('apagando: ', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('apagando: ', self.rua, self.numero)


cliente1 = Cliente('Samuel')
cliente1.inserir_enderecos('rua bolivar', 114)
cliente1.inserir_enderecos('Rua B', 6745)
endereco_externo = Endereco('rua das figueiras', 24)
cliente1.endereco_externo(endereco_externo)

print(cliente1.listar_endereco())
