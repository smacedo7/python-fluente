def recebe_numero(numero):
    def multiplica(multiplicador):
        return numero * multiplicador
    return multiplica


dobra = recebe_numero(1)
print(dobra(2))

triplica = recebe_numero(1)
print(triplica(3))

quadriplica = recebe_numero(1)
print(triplica(4))