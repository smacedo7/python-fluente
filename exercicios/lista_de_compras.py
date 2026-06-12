lista_de_compras = list()

opcao = ''
while opcao != 'C':
    print("""
    Selecione uma opção:

    [I]nserir
    [A]pagar
    [L]istar
    [C]ancelar
    """)
    opcao = input().upper().strip()
    if opcao not in 'IALC':
        print('Insira uma opçao valida! ')
  
    match opcao:
        case 'I':
            print('Insira qual item quer inserir na lista: ')
            item = input()
            lista_de_compras.append(item)
        case 'A':
            print('Insira o indice do item que quer apagar: ')
            item = int(input())
            if item > len(lista_de_compras):
                print('insira um indice valido')
            del lista_de_compras[item]
        case 'L':
            for contador, valor in enumerate(lista_de_compras):
                print(contador + 1, ': ', valor)

