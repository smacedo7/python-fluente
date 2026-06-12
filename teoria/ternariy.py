# Operaçao ternaria: condiconal de uma linha!
# <valor> if <condiçao> else <outro valor>

print('Valor' if True else 'Outro valor')  # Valor

condiçao = 10 == 10
variavel = 'Valor' if condiçao else 'Outro valor'
print(variavel)  # Valor

digito = 9
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('Valor' if True else 'Outro valor' if True else 'Fim')