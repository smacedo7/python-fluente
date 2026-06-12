# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

# s1 = set()
# print(s1, type(s1))  # set() <class 'set'>

# s1 = set('Luis')
# print(s1)  # {'i', 's', 'L', 'u'}

# s1 = {'Luis', 1, 2, 3}
# print(s1, type(s1))  # {'Luis', 1, 2, 3} <class 'set'>

# s1 = {1, 1, 1, 2, 2, 2, 4, 4}  # elimina duplicados
# print(s1)  # {1, 2, 4}

# s1 = [1, 1, 1, 3, 3, 4, 5]
# s2 = set(s1)
# l1 = list(s2)  # removi as repetiçoes e voltei a ter list

s1 = {1, 2}
s1.add('Samuel')
# print(s1)
# s1.update('Olá mundo! ')
# print(s1)  # {1, 2, 'u', '!', 'd', ' ', 'O', 'm', 'Samuel', 'n', 'á', 'l'}
s1.add(('Olá mundo', 1, 4, 6,))  # so aceita valores imutaveis, fazer tuple
# q nao buga
# print(s1)  # {'Samuel', 1, 2, ('Olá mundo', 1, 4, 6)}
# s1.clear()
s1.discard('Olá mundo')  # tenho q inserir um valor, nao vai sozinho

s3 = {1, 2, 3}
s4 = {2, 4, 1}
s5 = s3 | s4  # uniao
print(s5)  # uniao

s5 = s3 & s4  # intersecçao
print(s5)  # {1, 2}

s5 = s3 - s4  # unico elemento q esta presente em 3 e nao em 4
print(s5)  # {3}
s5 = s4 - s3  # unico elemento q esta presente em 3 e nao em 4
print(s5)  # {4}

s5 = s3 ^ s4  # itens q nao estao em ambos
print(s5)  # {3, 4}

# letras = set()
# while True:
#     letra = input('insira algum valor')
#     letras.add(letra)
#     print(letras)
