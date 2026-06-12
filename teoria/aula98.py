import aula98_m

import importlib  # pra importar 'mais de uma vez'
# recarrega o modulo basicamente


print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)
print('Fim! ')