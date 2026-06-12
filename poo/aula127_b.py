import json
from aula127_a import caminho_arquivo, Pessoa, fazendo_dump

# Primeiro ele executa o arquivo inteiro no import
fazendo_dump()  # executa so agora o dump

with open(caminho_arquivo, 'r') as arquivo:
    pessoas = json.load(arquivo)  # pessoas vai receber os dados
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)