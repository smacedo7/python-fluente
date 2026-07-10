# alguma forma de iterar sobre o objeto
# exemplo: 
# for item in objeto:
# itera sobre o objeto, nao sobre a lista dele
# sem o itter implementado, teria que iterar asim:
# for musica in objeto.playlist:

class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
    
    def __str__(self):
        return f"(Titulo={self.titulo}, Duracao={self.duracao}, Artista={self.artista})"


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []
    
    def __iter__(self):
        return iter(self.musicas)
    
    def adicionar(self, musica):
        self.musicas.append(musica)
    
    def remover(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)

    def __len__(self):
        return len(self.musicas)


playlist = Playlist("Favoritas")

playlist.adicionar(Musica("Música A", "Artista 1", 210))
playlist.adicionar(Musica("Música B", "Artista 2", 185))
playlist.adicionar(Musica("Música C", "Artista 3", 240))

for musica in playlist:
    print(musica)

print(len(playlist))