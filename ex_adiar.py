# def soma(x):
#     def cinco():
#         return x + 5
#     return cinco


# def executa(func, *args):
#     return func(args)


# somatorio = soma(5)
# print(somatorio())

def soma(x, y):
    return x + y


def multiplicaçao(x, y):
    return x * y


# def adia(funcao, y):
#     x = 5

#     def enrolada():
#         return funcao(x, y)
#     return enrolada


def adia(funcao, x):
    def enrolada(y):
        return funcao(x, y)
    return enrolada


soma_com_cinco = adia(soma, 5)
print(soma_com_cinco(10))

multiplicaçao_com_cinco = adia(multiplicaçao, 5)
print(multiplicaçao_com_cinco(10))


# soma_com_cinco = adia(soma, 10)
# multiplicaçao_com_cinco = adia(multiplicaçao, 10)
# print(soma_com_cinco())
# print(multiplicaçao_com_cinco())