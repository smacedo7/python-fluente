"""
Jogo da Forca com Listas de Strings em Python
Objetivo:

O objetivo deste exercício é criar uma versão do jogo da forca que utilize
listas de strings para desenhar o boneco. Você deve usar uma lista para cada linha
do desenho e organizá-las em uma lista de listas. Ao invés de controlar quando imprimir 
cada parte do boneco, você deve atualizar as listas, substituindo o elemento a ser desenhado.

Requisitos:

    1. Crie uma função chamada mostrar_tabuleiro que aceite como argumento o número 
    de erros do jogador. Esta função deve desenhar o estado atual do tabuleiro com o boneco.

    2. Utilize uma variável numero_de_erros para manter o controle do número de erros do jogador.

    3. O jogador deve continuar adivinhando letras até que:
        O número máximo de 6 erros seja alcançado, ou;
        A palavra seja completamente adivinhada.

    4. Utilize uma lista de strings para representar a palavra a ser adivinhada, 
    substituindo letras não adivinhadas por sublinhados ("_").

    5. Quando o jogo terminar, mostre uma mensagem informando se o jogador 
    ganhou ou perdeu, além de revelar a palavra que deveria ser adivinhada.

Dicas:

    Comece criando o tabuleiro em uma lista de listas, preenchendo 
    as partes que nunca mudam.
    
    Atualize o tabuleiro a cada erro do jogador, chamando a função 
    mostrar_tabuleiro com o número atual de erros como argumento.
"""


def mostrar_tabuleiro(erros):

    estado_atual = [
        [' ', ' ', ' ', ' ', ' ', ' ', '_'],  # Parte superior do poste
        [' ', ' ', ' ', ' ', ' ', '|', ' '],  # Poste vertical, parte 1
        [' ', ' ', ' ', ' ', ' ', '|', ' '],  # Poste vertical, parte 2 (onde a cabeça aparece)
        [' ', ' ', ' ', ' ', ' ', '|', ' '],  # Poste vertical, parte 3 (onde o corpo e os braços aparecem)
        [' ', ' ', ' ', ' ', ' ', '|', ' '],  # Poste vertical, parte 4 (onde as pernas aparecem)
        ['_', '_', '_', '_', '_', '|', ' ']   # Base e parte inferior do poste
    ]
    if erros >= 1:
        estado_atual[2][5] = "O"
    if erros >= 2:
        estado_atual[3][5] = "|"
    if erros >= 3:
        estado_atual[3][4] = '/'
    if erros >= 4:
        estado_atual[3][6] = '\\'
    if erros >= 5:
        estado_atual[4][4] = '/'
    if erros >= 6:
        estado_atual[4][6] = '\\'

    for linha in estado_atual:
        print("".join(linha))


palavra = input('insira uma palavra: ')
resposta = len(palavra) * ['_']

erros = 0

while erros < 6 and '_' in resposta:
    mostrar_tabuleiro(erros)
    print('palavra a acertar: ', ' '.join(resposta))
    letra = input('insira uma letra: ')
    if letra not in palavra:
        erros += 1
    else:
        for indice, chute in enumerate(palavra):
            if chute == letra:
                resposta[indice] = chute

mostrar_tabuleiro(erros)

if '_' in resposta:
    print('voce perdeu bot')
else:
    print('voce ganhou goat')
