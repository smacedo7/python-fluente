pessoas = [
    {"nome": "Samuel", "idade": 19},
    {"nome": "Ana", "idade": 25},
    {"nome": "João", "idade": 18},
]
# dictionary = {"nome": "Samuel", "idade": 19}
# print(dictionary["nome"])

# for dicionario in pessoas:
#     for chave in dicionario:
#         print(dicionario[chave])
pessoas2 = [
    {"nome": "Samuel", "idade": 19},
    {"nome": "Ana", "idade": 25},
    {"nome": "João", "idade": 18},
    {"nome": "Beatriz", "idade": 19},
]
ordered_ages2 = sorted(pessoas2, key=lambda pessoa: (pessoa["idade"], pessoa["nome"]))
# quando retorna uma tupla, o Python compara elemento por elemento, da esquerda para a direita.
print(*ordered_ages2, sep='\n')
print()

ordered_ages = sorted(pessoas, key=lambda x: x["idade"])
print(*ordered_ages, sep='\n')
# desempacotamento = pega a lista por exemplo e desempacota tudo que tem nela

print()
ordered_sizes = sorted(pessoas, key=lambda x: len(x["nome"]))
print(*ordered_sizes, sep='\n')

print()
ordered_letter = sorted(pessoas, key=lambda x: x["nome"])
print(*ordered_letter, sep='\n')