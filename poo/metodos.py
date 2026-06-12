# hard coded - é algo que pode ser escrito a força no code
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome

    # metodos
    def acelerar(self):
        print(f'{self.nome} está acelerando')


fusca = Carro('fusca')
celta = Carro(nome='Celtinha')
print()
print(fusca.nome)  # fusca

fusca.acelerar()  # fusca está acelerando
# metodo é uma funçao entao sempre executar,
# mas como metodo

Carro.acelerar(fusca)  # fusca está acelerando
print(celta.nome)  # Celtinha
