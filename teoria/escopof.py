"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

# x = 1


# def escopo():
#     def outro_escopo():
#         print(x)
#         y = 1
#         print(x + y)

#     outro_escopo()
#     print(x)


# escopo()

x = 1


def escopo():
    global x
    x = 10

    def outro_escopo():
        global x
        x = 11
        y = 5
        print(x)
        print(x + y)

    outro_escopo()
    print(x)


print(x)
escopo()
print(x)
