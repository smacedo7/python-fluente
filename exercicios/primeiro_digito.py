cpf = '74682489070'
nove_digitos = cpf[:9]
contador = 10

resultado_cpf1 = 0
for digito in nove_digitos:
    resultado_cpf1 += int(digito) * contador
    contador -= 1
digito1 = (resultado_cpf1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0
print(digito1)
