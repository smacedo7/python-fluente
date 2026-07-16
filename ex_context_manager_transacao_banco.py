class TransacaoBanco:
    def __enter__(self):
        print('Conectando ao banco...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:  # -> ta errado, classe exception sempre 
            print('rollback')
        else:
            print('commit realizado')


    def executar(self, sql):
        print(f'Executando {sql}')
    
with TransacaoBanco() as banco:  # a excecao vai ocorrer dentro do bloco do with, se ocorrer vai pro exit e trata ela la
    banco.executar('INSERT INTO usuarios VALUES (...)')

with TransacaoBanco() as banco:
    banco.executar("DELETE FROM usuarios")
    print(10 / 0)
