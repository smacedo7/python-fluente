def multiplicador(fator):
    # funçao interna,
    #  vai lembrar do parametro fator mesmo depois da funçao ter acabado
    def multiplicaçao(numero):
        return numero * fator

    return multiplicaçao


dobro = multiplicador(2)

print(dobro(5))


# def criar_saudacao(saudacao, nome):
#     def saudar():
#         return f'{saudacao}, {nome}'
#     return saudar()  # parenteses faz executar a funçao.

# def criar_saudacao(saudacao, nome):
#     def saudar():
#         return f'{saudacao}, {nome}'
#     return saudar  # sem parenteses


# s1 = criar_saudacao('Bom-dia', 'Luis')  # Bom-dia, Luis com parenteses ou
# # sem parenteses: <function criar_saudacao.<locals>.saudar at ...

# s2 = criar_saudacao('Boa noite', 'luna')

# print(s1)  # <function criar_saudacao.<locals>.saudar at 0x000001683797C3B0>
# print(s2())  # Boa noite, luna

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


v1 = criar_saudacao('Olá meu garoto! ')
# print(v1)  # <function criar_saudacao.<locals>.saudar at 0x0000018DBFA1C3B0>

print(v1('biel'))  # Olá meu garoto! , biel

for nome in ['gabriel', 'ganley', 'joao']:
    print(v1(nome))
