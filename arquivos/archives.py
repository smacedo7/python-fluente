from pathlib import Path
import os

os.chdir('/Users/samuelmacedo/Projetos/python/python-fluente/arquivos')
print(Path.cwd())  # /Users/samuelmacedo/Projetos/python/python-fluente/arquivos

"--------------------------------------------------------------------"
# objetos da class Path

p = Path('spam.txt')

p.write_text('hello world')

print(p.write_text('hello world'))  # retorna 11 pq 11 caracteres foram gravados

print(p.read_text())  # hello world

"--------------------------------------------------------------------"

# fiz um arquivo com o metodo write_text
# li o arquivo com o metodo read_text


# forma comum de gravar em arquivos: 

# 1. chamar a func open() para retornar objeto do tipo file -> na func tem que ter o caminho do arquivo
# 2. chamar o metodo read() ou write() sobre esse objeto file
# 3. fechar o arquivo com o metodo close() do objeto file

# modo leitura é o metodo padrao de abertura de arquivos py
# boa pratica sempre passar o encoding=utf-8
# modo de escrita = 'w'
# open(nome_do_arquivo, modo, encoding=utf-8)

"--------------------------------------------------------------------"

txt = Path(Path.cwd() / 'arquivo_txt.txt')

hello_file = open(txt, 'w', encoding='utf-8')  # se nao passar o 'w' vai dar erro pq o arquivo ainda nao foi criado
# aqui virou um objeto file, que representa um arquivo no nosso pc
# sempre que quisermos ler ou gravar dados no arquivo, basta chamar os metodos apropriados sobre o objeto file
hello_file.close()

"--------------------------------------------------------------------"

train_file = Path('training_two.txt')   # como ja estou no cd diretorio atual, o path ja completa automatico
print(train_file)  # training_two.txt
train_file.write_text('' \
                      'meu nome é slime' 
                      'quebrando linha'
'')

obj_file = open(train_file, 'w', encoding='utf-8') 
obj_file.close()

"--------------------------------------------------------------------"

bacon_file = 'bacon.txt'

receptor = open(Path.cwd() / bacon_file, 'a', encoding='utf-8')
receptor.write('bixcoito')
receptor.close()
"--------------------------------------------------------------------"
pancakes = Path('pancakes.txt')

hooney = open(pancakes, 'a', encoding='utf-8')  # nao da pra ler aqui
hooney.write('i love pancake recipe')
hooney.close()
hooney = open(pancakes, encoding='utf8')
content = hooney.read()
hooney.close()
print(content)

"--------------------------------------------------------------------"

# intrucao with:
# sempre fecha o arquivo apos execucao;

pokeball = 'with.txt'

with open(pokeball, 'a', encoding='utf-8') as ash:  # caminho arquivo e objeto file depois
    ash.write('gotcha in all!')

# variavel é criada so no final!

"--------------------------------------------------------------------"
