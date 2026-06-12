# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def inverte_string(string):
    return string[::-1]


def is_string(string):
    if not isinstance(string, str):
        raise TypeError('deve ser uma string')


def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorar')
        for arg in args:
            is_string(arg)
        print('voce foi decorado')
        resultado = func(*args, **kwargs)
        print(resultado)
        return resultado
    return interna


checa_parametro_inverte = criar_funcao(inverte_string)
invertida = checa_parametro_inverte('123')
print(invertida)  # leumas
