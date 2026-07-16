from abc import abstractmethod, ABC

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
        self.conta = None  # cliente tem uma conta


class Conta(ABC):
    def __init__(self, agencia, numero_da_conta, saldo):
        super().__init__()
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self):
        pass

    def deposito(self, valor):
        self.saldo += valor
        return self.saldo


class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass


class Banco:
    def __init__(self, agencias):
        self.agencias = agencias
        self.clientes = []
        self.contas = []

    def _verifica_agencias(self, conta):
        return conta.agencia in self.agencias
    
    def _verifica_clientes(self, cliente):
        return cliente in self.clientes
    
    def _verifica_contas(self, conta):
        return conta in self.contas
    
    def verificacao(self, conta, cliente):
        return (
            self._verifica_agencias(conta)
            and self._verifica_contas(conta)
            and self._verifica_clientes(cliente)
            and cliente.conta is conta  # essa conta é do cliente? 
        )



"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""