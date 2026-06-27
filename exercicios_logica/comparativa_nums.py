
# Exercício - Análise Comparativa e Estatística de Números

# Objetivo: Desenvolver um programa que obtenha do usuário dez números e realize 
# análises estatísticas e matemáticas com base nos valores inseridos.

# Instruções:

#     1. Solicite ao usuário que informe dez números.
#     2. Determine e exiba qual é o maior número.
#     3. Determine e exiba qual é o menor número.
#     4. Calcule e exiba a média dos dez números.
#     5. Informe quantos dos números são pares.
#     6. Informe quantos dos números são positivos.
#     7. Calcule e exiba a variação (diferença) entre o maior e o menor número.
#     8. Mostre a soma dos números que são maiores que a média.
#     9. Informe quantos dos números são negativos.
    
# Observações: O programa deve considerar que o usuário fornecerá apenas 
# valores numéricos válidos. Em todas as operações, os resultados devem ser 
# exibidos com até duas casas decimais, quando aplicável.

lista = []
par = []
impar = []
positivos = []
negativos = []

for i in range(11):
    numero = int(input('insira um numero: '))
    lista.append(numero)
    if numero > 0:
        positivos.append(numero)
    else:
        negativos.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print('maior: ', max(lista))
print('menor: ', min(lista))

media = sum(lista) / len(lista)
print('a media é: ', media)
print(f'os numeros pare sao: {par}, {len(par)}, numero(s)')
print(f'positivos: {positivos}, {len(positivos)}')
print(f'diferença entre {max(lista)} e {min(lista)} = ', end='')
print(max(lista) - min(lista))

maior = []
for i in lista:
    if i > media:
        maior.append(i)

print(f'a soma dos numeros maiores que a média: {sum(maior)}')
print(f'temos {len(negativos)} numero(s) negativo(s)')
