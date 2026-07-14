from pathlib import Path
import os

os.chdir('/Users/samuelmacedo/Projetos/python/python-fluente/arquivos')
print(Path.cwd())  # /Users/samuelmacedo/Projetos/python/python-fluente/arquivos

p = Path('spam.txt')

p.write_text('hello world')

print(p.write_text('hello world'))  # retorna 11 pq 11 caracteres foram gravados

print(p.read_text())  # hello world

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

txt = Path(Path.cwd() / 'arquivo_txt.txt')

hello_file = open(txt, 'w', encoding='utf-8')  # se nao passar o 'w' vai dar erro pq o arquivo ainda nao foi criado
# aqui virou um objeto file, que representa um arquivo no nosso pc
# sempre que quisermos ler ou gravar dados no arquivo, basta chamar os metodos apropriados sobre o objeto file