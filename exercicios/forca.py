import os

palavra_secreta = 'python'
letras_acertadas = ''
print('Bora! ')
numero_de_tentativas = 0
while True:
    
    numero_de_tentativas += 1
    letra_digitada = input('insira uma letra: ')

    if len(letra_digitada) > 1 or letra_digitada.isnumeric():
        print('digite apenas uma letra ou insira um caractere valido! ')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Parabéns! Você acertou a palavra! ')
        print('A palavra era:', palavra_formada)
        print("Numero de tentativas: ", numero_de_tentativas)
        letras_acertadas = ''
        numero_de_tentativas = 0