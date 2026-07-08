def log(func):
    print("entrando no log")
    def executar(*args, **kwargs):
        print("dentro da que executa interna! ")
        print(f"executando {func.__name__}")
        return func(*args, **kwargs)
    return executar


@log
def multiplicar(a, b):
    return a * b

@log
def saudacao(nome, emoji="👋"):
    return f"Olá {nome}, {emoji}"             

@log
def soma(*args):
    print("Dentro da func soma")
    return sum(args)

print(multiplicar(20, 3))
print(soma(4, 5))
# print(executar(soma, 10, 20, 30, 40))
# print(executar(multiplicar, 6, 7))
# print(executar(saudacao, "pirralho", "crioulo"))
# print(executar(saudacao, "Samuel", emoji="🚀"))
