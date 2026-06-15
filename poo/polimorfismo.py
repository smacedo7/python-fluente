# assinatura de um metodo: Nome do método + parâmetros que ele recebe
# def somar(self, x, y):
#     pass

# A assinatura é:

# somar(self, x, y)

# Liskov Substitution Principle (LSP):
# "Objetos de uma classe derivada devem poder substituir "
# "objetos da classe base sem quebrar o programa."

# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅

from abc import ABC, abstractmethod


class Animal:
    def falar(self):
        raise NotImplementedError


class Cachorro(Animal):
    def falar(self):
        print('Au au')


class Gato(Animal):
    def falar(self):
        print('Miau')


def fazer_falar(animal):
    animal.falar()


c = Cachorro()
g = Gato()

fazer_falar(c)
fazer_falar(g)


class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)

# "A mesma chamada pode produzir comportamentos
# diferentes dependendo do objeto."
# Muitas implementações para a mesma operação.
# falar()
# ├── Cachorro -> Au au
# ├── Gato -> Miau
# └── Papagaio -> Curupaco


class Personagem:
    def atacar(self):
        pass


class Guerreiro(Personagem):
    def atacar(self):
        print('Espadada')


class Arqueiro(Personagem):
    def atacar(self):
        print('Flechada')


class Mago(Personagem):
    def atacar(self):
        print('Bola de fogo')

# Visualmente:

# atacar()
# ├── Guerreiro -> Espadada
# ├── Arqueiro -> Flechada
# └── Mago -> Bola de fogo

# Polimorfismo É:
# várias classes responderem à mesma mensagem
# cada uma do seu jeito