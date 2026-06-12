def par_ou_impar(numero):
    return 'é par' if numero % 2 == 0 else 'É ímpar'


numero1 = par_ou_impar(2)
print(numero1)

numero2 = par_ou_impar(3)
print(numero2)


def impar_ou_par(numero):
    return True if numero % 2 == 0 else False


numero3 = impar_ou_par(4)
numero4 = impar_ou_par(5)
print(numero3)
print(numero4)