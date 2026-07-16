class MeuOpen:
    def __init__(self, caminho, modo):
        self.caminho = caminho
        self.modo = modo
        self.arquivo = None  # troca o valor do objeto

    def __enter__(self):
        print('Abrindo aquivo...')
        self.arquivo = open(self.caminho, self.modo)
        return self.arquivo

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            print(f'Houve uma exceção {exc_type}')
        print('Fechando arquivo! ')
        self.arquivo.close()
    


with MeuOpen("usuarios.txt", "a") as arq:
    arq.write("Samuel\n")

with MeuOpen("usuarios.txt", "a") as arq:
    arq.write("Maria\n")
    print(10 / 0)