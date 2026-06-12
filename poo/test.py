class Pessoa:
    def falar(self):
        print('oi')


p1 = Pessoa()
p1.falar()  # oi
Pessoa.falar(p1)  # oi


class Teste:
    @classmethod
    def teste(cls):
        print(cls)


Teste.teste()


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()  # Connection()
        connection.user = user
        connection.password = password
        return connection


p1 = Connection()
p1.set_user('pedro')
print(p1.user)  # pedro

personagem1 = Connection.create_with_auth('slime', 1234)
# return classe fez ele virar a classe Connection

print(personagem1.user)
print(personagem1.host)


class Usuario():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_por_ano(cls, nome, ano):
        idade = 2026 - ano
        return cls(nome, idade)


pessoa_nova = Usuario.criar_por_ano('samuel', 19)
print(pessoa_nova.nome)