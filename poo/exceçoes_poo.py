# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MeuError(Exception):  # Exception: classe de erro! 
    # Meu error é um tipo de erro pq excepetion é a classe base de erros do py
    ...


class OutroError(Exception):
    ...


def levantar():
    exception_ = MeuError('a', 'b', 'c')  # cria um objeto de erro da classe
    # MeuError
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:  # valores a b e c ficam
    # guardados em error
    print(error.__class__.__name__)
    print(error.args)  # a b c desempacotamento
    print()
    exception_ = OutroError('Vou lançar de novo')  # cria objeto
    raise exception_ from error  # lança esse erro agora
    # OutroError: Vou lançar de novo
