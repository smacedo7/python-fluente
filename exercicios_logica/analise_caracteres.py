"""
Exercício: Análise de Caracteres e Formação de Palavras

Objetivo: Desenvolver um programa que obtenha do usuário uma letra ou uma
palavra
e realize análises sobre o tipo de caractere inserido, além de funções
adicionais
se uma palavra completa for fornecida.

Instruções:

    1. Solicite ao usuário que digite uma letra ou uma palavra.
    
    2. Se o usuário digitar apenas um caractere:
    
        a. Verifique se é uma vogal ou consoante.
        b. Se for uma vogal, exiba: "Você digitou uma vogal."
        c. Se for uma consoante, exiba: "Você digitou uma consoante."
        d. Se o caractere não for uma letra, exiba: "Caractere inválido."
    
    3. Se o usuário digitar mais de um caractere (uma palavra):
        
        a. Calcule e exiba o número de vogais na palavra.
        b. Calcule e exiba o número de consoantes na palavra.
        c. Exiba a palavra em ordem inversa.
        d. Informe se a palavra é um palíndromo (se lê da mesma forma de frente para trás 
        e de trás 
        para frente, como "arara").
    
    4. Peça ao usuário se deseja verificar outra letra ou palavra ou sair do programa.

Observações: O programa deve considerar letras maiúsculas e 
minúsculas (ou seja, "A" e "a" são ambas vogais).
"""

entrada = input("insira uma letra ou uma palavra: ")

vogal = 'aeiou'
consoante = 'bcdfghjklmnpqrstvwxyz'

if len(entrada) == 1:
    if entrada in vogal:
        print('Voce digitou uma vogal')
    elif entrada in consoante:
        print('voce digitou uma consoante')
    else:
        print('Caractere invalido')
else:
    somav = 0
    somac = 0
    for i in entrada:
        if i in vogal:
            somav += 1
        if i in consoante:
            somac += 1
    print(f'a palavra tem {somac} consoantes! ')
    print(f'a palavra tem {somav} vogais!')

print(entrada[::-1])

if entrada == entrada[::-1]:
    print('é palindromo')