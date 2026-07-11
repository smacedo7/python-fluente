class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
    
    def __str__(self):
        return (
            f"{self.titulo} - {self.artista} - {self.duracao}"
        )


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []
    
    def adicionar(self, musica):
        self.musicas.append(musica)
    
    def __iter__(self):
        return iter(self.musicas)

playlist = Playlist("Favoritas")

playlist.adicionar(
    Musica("Bohemian Rhapsody", "Queen", 354)
)

playlist.adicionar(
    Musica("Imagine", "John Lennon", 183)
)

playlist.adicionar(
    Musica("Numb", "Linkin Park", 185)
)

for musica in playlist:
    print(musica)