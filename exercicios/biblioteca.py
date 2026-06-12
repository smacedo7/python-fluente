# primeiro entra no atributo do objeto l1.__dict__ e se nao acha nada
# ele nao pertence ao objeto e vai procurar na classe Livro.__dict__
import json


class Livro:
    total_livros = 0
    todos_os_livros = []

    def __init__(self, titulo, autor, ano):  # roda logo quando o objeto nasce
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        Livro.total_livros += 1  # assim q inicializa o init ja add no contador
        Livro.todos_os_livros.append(self)

    def dados(self):
        return f'{self.titulo} - {self.autor} ({self.ano})'

    @classmethod
    def from_string(cls, text):
        titulo, autor, ano = text.split('|')
        return cls(titulo, autor, int(ano))

    @staticmethod
    def validar_ano(ano):
        if ano < 0 or ano > 2026:
            return False
        return True

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dados):
        return cls(**dados)


if __name__ == '__main__':
    caminho = 'biblioteca.json'

    l1 = Livro('1984', 'George Orwell', 1949)
    l2 = Livro('O Hobbit', 'Tolkien', 1937)
    l3 = Livro.from_string('Dom Casmurro|Machado de Assis|1899')

    print(Livro.total_livros)

    print(l1.dados())

    print(Livro.validar_ano(2006))

    lista = [livro.to_dict() for livro in Livro.todos_os_livros]

    with open(caminho, 'w', encoding='utf8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)

    with open(caminho, 'r', encoding='utf8') as arquivo:
        json_dados = json.load(arquivo)

    livros_carregados = [
        Livro.from_dict(dados)
        for dados in json_dados
    ]

    for book in livros_carregados:
        print(book.dados())
