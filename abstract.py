from abc import ABC, abstractmethod


class AssistenteVirtual(ABC):

    @abstractmethod
    def responder_comando(self, comando):
        pass


class Jarvis(AssistenteVirtual):

    def responder_comando(self, comando):
        print(f"Executando o comando: {comando}")


# AssistenteVirtual é uma classe abstrata: ou seja,
# ela define o que deve ser feito, mas não implementa os detalhes.
# @abstractmethod marca o método que precisa ser
# implementado por qualquer classe que herde de AssistenteVirtual.
# Jarvis é quem realmente implementa a lógica,
# dizendo o que fazer com o comando.
