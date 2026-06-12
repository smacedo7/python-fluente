import re
import sys

entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Entrada é sequencial')
    sys.exit()
    
nove_digitos = cpf_enviado_usuario[:9]
contador1 = 10

resultado_cpf1 = 0
for digito in nove_digitos:
    resultado_cpf1 += int(digito) * contador1
    contador1 -= 1
digito1 = (resultado_cpf1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0
print(digito1)

dez_digitos = cpf_enviado_usuario[:10]
contador2 = 11
resultado_cpf2 = 0

for digito in dez_digitos:
    resultado_cpf2 += int(digito) * contador2
    contador2 -= 1
digito2 = (resultado_cpf2 * 10) % 11
digito2 = digito2 if digito2 > 9 else 0
print(digito2)

cpf_gerado = f'{nove_digitos}{digito1}{digito2}'
print('o cpf gerado é: ', cpf_gerado)
if cpf_gerado != cpf_enviado_usuario:
    print('CPF INVÁLIDO! ')
else:
    print('CPF VÁLIDO')