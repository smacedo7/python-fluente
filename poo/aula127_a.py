import json


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


caminho_arquivo = 'aula127.json'

p1 = Pessoa('Samuel', 19)
p2 = Pessoa('Joao', 20)
p3 = Pessoa('Ana', 18)

lista = [vars(p1), p2.__dict__, p3.__dict__]  # se passar so a lista da erro


def fazendo_dump():
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)

        # O parâmetro ensure_ascii=False é usado no módulo json do Python
        # para permitir que caracteres especiais e acentuados sejam exibidos
        # corretamente em arquivos
