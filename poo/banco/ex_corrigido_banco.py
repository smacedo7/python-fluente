from abc import ABC, abstractmethod


# =====================
# PESSOA / CLIENTE
# =====================

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None  # cliente TEM uma conta


# =====================
# CONTAS
# =====================

class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite=500):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > (self.saldo + self.limite):
            raise ValueError('Saldo + limite insuficiente')

        self.saldo -= valor
        return self.saldo


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError('Saldo insuficiente')

        self.saldo -= valor
        return self.saldo


class Banco:
    def __init__(self, agencias):
        self.agencias = agencias
        self.clientes = []
        self.contas = []

    def autenticar(self, cliente, conta):
        return (
            conta.agencia in self.agencias and
            cliente in self.clientes and
            conta in self.contas and
            cliente.conta is conta
        )

    def sacar(self, cliente, conta, valor):
        if not self.autenticar(cliente, conta):
            print('Acesso negado')
            return

        return conta.sacar(valor)

    def depositar(self, cliente, conta, valor):
        if not self.autenticar(cliente, conta):
            print('Acesso negado')
            return

        return conta.depositar(valor)


# criando banco
banco = Banco([123])

# criando cliente
cliente = Cliente("Samuel", 19)

# criando conta
conta = ContaCorrente(123, 1, 1000)

# ligando cliente à conta
cliente.conta = conta

# registrando no banco
banco.clientes.append(cliente)
banco.contas.append(conta)

# operações
print(banco.sacar(cliente, conta, 200))   # saque
print(banco.depositar(cliente, conta, 500))  # depósito