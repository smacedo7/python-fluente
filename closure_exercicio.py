def criar_potencia(numero):
    def multiplicando(multiplo):
        return multiplo ** numero
    return multiplicando

quadrado = criar_potencia(2)
cubo = criar_potencia(3)

print(cubo(5))
print(quadrado(5))
