from pathlib import Path
import os


def limpa_tela():
    os.system('clear')


print(Path('coco_limao'))  # coco_limao  so retorna a string literalmente

print(str(Path('spam', 'bacon', 'eggs')))  # retorna: spam/bacon/eggs -> um objeto path, retorna caminho deles

print(Path('spam') / 'bacon' / 'eggs')  # para concatenar obj path e 2 strings: spam/bacon/eggs

print(Path('spam') / Path('bacon/eggs'))  # spam/bacon/eggs

print(Path('spam') / Path('bacon', 'eggs'))  #  spam/bacon/eggs

print(Path.home())  # retorna path da home -> /Users/samuelmacedo

print(Path.cwd())  # /Users/samuelmacedo/Projetos/python/python-fluente -> retorna diretorio atual

os.chdir('/Users/samuelmacedo/Projetos/python')
print(Path.cwd())  # /Users/samuelmacedo/Projetos/python -> alterou diretorio pra ca

# os.mkdir()  # cria um diretorio

print(Path.cwd().is_absolute())