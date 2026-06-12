class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print('Já esta filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} nao esta filmando...')
            return
        
        print('Estou parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print('nao pode fotografar filmando')
            return

        print(f'{self.nome} esta fotografando...')


print()
c1 = Camera('sony')
c2 = Camera('canon')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print(c1.filmando)  # atributo da classe
print(c2.filmando)