import os


def listar(lista):
    print()
    if not lista:
        print('nada para retornar')
        return

    for tarefa in lista:
        print(tarefa)
    print()


def desfazer(tarefas_refazer, tarefas):
    print()
    if not tarefas:
        print('sem tarefas para refazer! ')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista com sucesso')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas_refazer, tarefas):
    print()
    if not tarefas_refazer:
        print('sem tarefas para refazer! ')
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print('tarefa adicionada novamente! ')


def adicionar(tarefa, tarefas):
    tarefa = input('insira a tarefa a ser adicionada: ')
    tarefas.append(tarefa)


tarefas_refazer = []
tarefas = []
while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
    elif tarefa == 'desfazer':
        desfazer(tarefas_refazer, tarefas)
        listar(tarefas)
    elif tarefa == 'refazer':
        refazer(tarefas_refazer, tarefas)
        listar(tarefas)
    elif tarefa == 'clear':
        os.system('cls')
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
