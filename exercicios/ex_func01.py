# def multiplica(*args):
#     total = 0
#     for numero in args:
#         print(f'numero: {numero}')
#         total = numero if total == 0 else total * numero
#         print(f'total aual = {total}')
#     return total


# exemplo = multiplica(2, 3, 6)
# print(exemplo)

def multiplicaçao(*args):
    total = 1
    for i in args:
        print(i)
        total *= i
        print(f'O novo total é: ', total)
    return total


multiplicaçao(1, 2, 3, 4, 5)