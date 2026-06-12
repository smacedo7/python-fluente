"""
Higher Order Functions
- Funções que podem receber e/ou retornar outras funções

Funções de primeira classe
- Funções que são tratadas como outros tipos de dados comuns (strings,
 inteiros, etc...)
"""


# def saudacao(msg):
#     return msg


# def executa(funcao, texto):
#     return funcao()  # da erro, precisa do funcao(texto)

# def executa(funcao, texto):
#     return funcao(texto)


# saudacao2 = saudacao  # saudacao 2 agora virou uma funçao
# v = saudacao2('Olá, bom-dia! ')
# print(v)

# v = executa(saudacao, 'my name is barry')
# print(v)  # my name is barry

def saudacao(msg, nome):
    return f'{msg}, {nome}'


# def executa(funcao, *args):
#     return funcao(args)  # da erro pq nao desempacotou

def executa(funcao, *args):  # high order function
    return funcao(*args)


print(
    executa(saudacao, 'Hello my friends', 'Mr. Pinoquio')
)
print(
    executa(saudacao, 'Sou o mr lean', 'come to my room')
)
