class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

        @property
        def ferramenta(self):
            return self._ferramenta
    
        @ferramenta.setter
        def ferramenta(self, ferramenta):
            self._ferramenta = ferramenta


class Ferramenta:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} esta escrevendo'


escritor1 = Escritor('Samuel')
escritor1.ferramenta = 'Machado'
print(escritor1.ferramenta)  # machado
ferramenta1 = Ferramenta('Caneta bic')
print(ferramenta1.escrever())

maquina_de_escrever = Ferramenta('maquina')
escritor1.ferramenta = maquina_de_escrever
print(escritor1.ferramenta.escrever())  # isso é privado

# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.
