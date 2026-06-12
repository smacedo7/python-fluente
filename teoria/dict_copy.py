import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

# d2 = d1.copy()  # shallow copy, so copia os imutaveis,
# os mutaveis ainda sao apontados pra mesma coisa na memoria
# shallow copy = copia rasa

d2 = copy.deepcopy(d1)
