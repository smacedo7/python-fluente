
import os

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)

# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)

# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho = 'C:\\Users\\samuc\\Desktop\\atencao\\'
caminho += 'arquvivos.txt'
# criar pasta para armazenar arquivos e achar de onde vem
# caminho += sempre com o nome do arquivo py

# arquivo = open(caminho, 'w')  # sempre dois argumentos!
# arquivo.close()

# with open(caminho, 'w') as arquivo:
#     # print('Olá mundo')
#     # print('Fechando arquivo')
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')

with open(caminho, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('lendo! ')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

with open(caminho, 'r') as arquivo:
    print(arquivo.read())

# gerenciador de contexto logo acima:
# O with garante que o arquivo será fechado mesmo se ocorrer um erro.
# como se fosse um try: ... finally: arquivo.close()
# cuidado com as barras invertidas

# seek usado para mover o cursor ou ponteiro interno de um arquivo.
# Ele permite que você leia ou escreva em partes específicas de um arquivo

with open(caminho, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'Linha 4\n')
    )

# encoding é pra arquivo nao bugar formatação

# os.unlink(caminho)
# ou os.remove()
# os.rename(caminho, 'novo nome')