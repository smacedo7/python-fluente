from pathlib import Path
import os

def limparTela():
    os.system('clear')

"--------------------------------------------------------------------"


Path('spam', 'bacon', 'eggs')  # /usr/bin/python3 /Users/samuelmacedo/Projetos/python/python-f
# luente/arquivos/path.py

print(str(Path('spam', 'bacon', 'eggs')))


"--------------------------------------------------------------------"

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

# dois .. significam a pasta pai
# unico ponto . siginifica a pasta atual
# caminho relativo parte do diretorio atuak
# caminho absoluto parte da pasta raiz

"--------------------------------------------------------------------"
# criar uma nova pasta:

# os.mkdir('/Users/samuelmacedo/Projetos/python/python-fluente/arquivos/ruffles')  # criou ruffles HAHAHAH
print(Path.cwd())

# ou 

Path(r'/Users/samuelmacedo/Projetos/python/python-fluente/arquivos/fantinha').mkdir(exist_ok=True)  # cria tambem HAHAHAH

# para criar varias pastas: 

# Path(r'/Users/samuelmacedo/Projetos/python/python-fluente/arquivos/fantinha').mkdir(parents=True, exist_ok=True)
"--------------------------------------------------------------------"

# para saber se é o caminho absoluto:

print(Path.cwd().is_absolute())  # True

print(Path('bacon/molester/cheesecake').is_absolute())  # False
