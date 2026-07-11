from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass


class Carro(Veiculo):

    def ligar(self):
        return f"{self.__class__.__name__} ligando."

 
class Moto(Veiculo):

    def ligar(self):
        return f"{self.__class__.__name__} ligando."


class Caminhao(Veiculo):

    def ligar(self):
        return f"{self.__class__.__name__} ligando."


carro = Carro()
moto = Moto()
caminhao = Caminhao()

print(carro.ligar())
print(moto.ligar())
print(caminhao.ligar())

# classe abstrata funcao: 
# apenas para padronizar o comportamento de outras classes filhas
# garantindo que elas tenham os mesmo atributos (metodos obrigatorios)
# os metodos da classe abstrata sao todos vazios (pass)
# nao deixa instanciar ela pq ta marcada com o abstract method
# ou seja, é uma classe incompleta
 