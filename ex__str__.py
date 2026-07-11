class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def __str__(self):
        return f"""
        Livro: {self.titulo}
        Autor: {self.autor}
        Ano: {self.ano}
        """
    
    # def __repr__(self):
    #     return f"""
    #     Livro: {self.titulo}
    #     Autor: {self.autor}
    #     Ano: {self.ano}
    #     """

    def __repr__(self):
        return (
            f"Livro("
            f"titulo= {self.titulo!r}, "
            f"autor= {self.autor!r}, "
            f"ano= {self.ano!r}) "
        )

livros = [
    Livro("Python Fluente", "Luciano Ramalho", 2022),
    Livro("Clean Code", "Robert C. Martin", 2008)
]

print(livros)

# !r é para pedir pra usar repr primeiro 
