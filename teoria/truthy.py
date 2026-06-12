# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def falsy(valor):
    return 'falsy' if not valor else 'truthy'


print(f'Teste', falsy('TESTE'))  # STRING - TRUTHY
print(f'lista, {lista=}', falsy(lista))  # lista=[] falsy
print(f'dicionario, {dicionario=}', falsy(dicionario))  # dicionario={} falsy
print(f'conjunto, {conjunto=}', falsy(conjunto))  # dicionario={} falsy
print(f'tupla, {tupla=}', falsy(tupla))  # tupla, tupla=() falsy
print(f'string, {string=}', falsy(string))  # string, string='' falsy
print(f'inteito, {inteito=}', falsy(inteito))  # inteito, inteito=0 falsy
print(f'flutuante, {flutuante=}', falsy(flutuante))  # flutuante=0.0 falsy
print(f'nada=none, {nada=}', falsy(nada))  # nada=None falsy
print(f'falso, {falso=}', falsy(falso))  # falso=False falsy
print(f'intervalo, {intervalo=}', falsy(intervalo))  # intervalo=range(0, 0) falsy
