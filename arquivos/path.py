from pathlib import Path
import os

def limparTela():
    os.system('clear')

Path('spam', 'bacon', 'eggs')  # /usr/bin/python3 /Users/samuelmacedo/Projetos/python/python-f
# luente/arquivos/path.py

print(str(Path('spam', 'bacon', 'eggs')))

# concatenar caminhos\
# pode ser usado em dois objetos path, um objeto path e uma string mas nunca
# por duas strings, visto que resulta em erro 
# objeto path -> Path("objeto")

print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon/eggs'))
print(Path('spam') / Path('bacon', 'eggs'))

limparTela()

"--------------------------------------------------------------------"


# obter diretorio atual: 

print(Path.cwd())  # /Users/samuelmacedo/Projetos/python/python-fluente
print(os.getcwd())  # /Users/samuelmacedo/Projetos/python/python-fluente

"--------------------------------------------------------------------"
# alterar diretorio atual: 

os.chdir('/Users/samuelmacedo/Projetos/python')  # sai de python e voltei para python fluente
# os.chdir é os.change directory


print(Path.cwd())  # /Users/samuelmacedo/Projetos/python, esse apresenta o diretorio atual
# diretorios sempre entre aspas

"--------------------------------------------------------------------"

# acessar diretorio pessoal:

print(Path.home())  # /Users/samuelmacedo

limparTela()

"--------------------------------------------------------------------"
