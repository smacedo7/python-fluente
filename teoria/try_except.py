# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    print('LINHA 1')
    c = a / b
    print('LINHA 2')
except ZeroDivisionError:
    print('dividiu por zero')
except NameError:
    print('B nao está definido.')
except (TypeError, IndexError) as error:
    print('erro de tipo! ')
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)
except Exception:
    print('Erro desconhecido')