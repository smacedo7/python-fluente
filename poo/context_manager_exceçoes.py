# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...
class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_exception)  # classe do erro
        # print(exception_)  # mensagem do erro ou objeto do erro
        # print(traceback_)  # caminho das linhas ate o erro
        # exception_.add_note('Minha nota')

        # return True  # Tratei a exceção


with MyOpen('aula149.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 2\n', 123)  # mesmo dando erro, chama o exit
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)

# class_exception  # classe do erro: TypeError
# exception_       # objeto do erro: mensagem do erro
# traceback_       # caminho das linhas até o erro

# O principal trabalho de um Context Manager não é abrir o recurso.
# É garantir que ele seja liberado mesmo quando algo dá errado.

# def __exit__(self, banana, maca, abacaxi):
# Os nomes não importam.
# A quantidade de parâmetros importa.
# sempre passar