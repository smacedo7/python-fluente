# def inverte(frase):
#     splitada = frase.split()
#     atualizada = []
#     for palavra in splitada:
#         if len(palavra) >= 5:
#             atualizada.append(palavra[::-1])
#         else:
#             atualizada.append(palavra)
#     return ' '.join(atualizada)
def inverte(frase):
    return ' '.join(palavra[::-1] if len(palavra) >= 5 else palavra
                    for palavra in frase.split())


print(inverte('Hey fellow warriors'))