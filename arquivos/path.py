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
# parents=True é para criar as pastas familiares automaticamente 
"--------------------------------------------------------------------"

# para saber se é o caminho absoluto:
# caminho relativo é tudo que parte do diretorio atual!
# caminho absoluto comeca pela pasta raiz

print(Path.cwd().is_absolute())  # True

print(Path('bacon/molester/cheesecake').is_absolute())  # False

limparTela()
"--------------------------------------------------------------------"
# encontrar caminho absoluto a partir de um caminnho relativo:

print(Path.cwd())  # /Users/samuelmacedo/Projetos/python

print(Path.cwd() / Path('my/relative/path'))  # /Users/samuelmacedo/Projetos/python/my/relative/path
# todo o caminho absoluto desde a base ate a pasta que passamos

print(Path('my/relative/path').absolute())  # /Users/samuelmacedo/Projetos/python/my/relative/path
# todo caminho absoluto desde a pasta relativa, ou seja, tudo para tras

print(Path.home() / Path('my/relative/path'))  # /Users/samuelmacedo/my/relative/path
# mesma coisa, tudo da relativa para tras

limparTela()

"--------------------------------------------------------------------"
# partes de um arquivo: 

# pasta raiz do sistema de arquuivos
# pasta pai
# nome do arquivo com extensao
# sao atributos, nao precisa de parenteses no final

# anchor, parent, name, stem, suffix, drive

# para extrair cada parte desse arquivo:

print(Path.cwd())  # /Users/samuelmacedo/Projetos/python

print(Path.cwd().anchor)  # /
print(Path.cwd().name)  # python
print(Path.cwd().parent)  # /Users/samuelmacedo/Projetos podemos acessar com o indice numerico tipo parents[0]
print(Path.cwd().stem)  # python
print(Path.cwd().suffix)  # sem
print(Path.cwd().drive)  # sem

# dividir por partes com o atributo: 

print(Path.cwd().parts)  # ('/', 'Users', 'samuelmacedo', 'Projetos', 'python')
# retorna tupla que pode ser acessada por indices
"--------------------------------------------------------------------"

# localizar arquivos com padrao glob:

# '*' faz correspondencia com qualquer sequencia de texto
# '?' faz correspondencia com somente um caractere
# *.txt -> faz correspondencia com qualquer que acaba com txt
# project*.txt -> faz correspondencia com project1.txt e projectx.txt

limparTela()
"--------------------------------------------------------------------"

# verificar veracidade de um caminho: 
# adota-se p como uma variavel que é objeto de path
# usam-se metodos, nao atributos.


p = Path.cwd()
print(p)  # /Users/samuelmacedo/Projetos/python

print(p.exists())  # True -> retorna True se o caminho existir
print(p.is_dir())  # True  -> returna True se o caminho existir e for um diretorio
print(p.is_file())  # False -> retorna True o caminho existir e for um arquivo

"--------------------------------------------------------------------"

# processo de leitura e gravacao de arquivos:
# arquivos de texto simples com .txt ou .py
# arquivos binarios sao aqueles que guardam bytes, e nao texto diretamente legivel.
# exemplo: imagens, videos, audios, pdfs
