# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')  # ['luiz', 'Joana']

cliente2 = adiciona_clientes('helena') # ['luiz', 'Joana', 'helena']
adiciona_clientes('Mario', cliente2)
cliente3 = adiciona_clientes('moreira')  # ['luiz', 'Joana', 'helena', 'Mario']
adiciona_clientes('vivi', cliente3)  # ['luiz', 'Joana', 'helena', 'Mario']

# a lista vai ser sempre a mesma

# se fazendo uma funçao o parametro ser mutavel
# sempre deixar ele None

print(cliente1)
print(cliente2)
print(cliente3)