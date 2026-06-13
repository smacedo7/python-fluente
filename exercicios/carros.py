class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, marca):
        self._fabricante = marca


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.lista_carros = []

    def adiciona_carros(self, *carros):
        for carro in carros:
            self.lista_carros.append(carro)


fusca = Carro('fusca')
fusca.fabricante = 'volkswagen'
print(fusca.fabricante)
motor = Motor('1.0')

fusca.motor = motor
print(fusca.nome)
print(fusca.fabricante)

print(fusca.nome, fusca.fabricante, fusca.motor)