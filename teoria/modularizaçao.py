# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

# import modularizaçao_m
# import sys


# print(sys.path)  
# ['c:\\Users\\samuc\\Desktop\\teoria\\teoria', 'C:
# \\Users\\samuc\\AppData\\Local\\Programs\\Python\\Python314\\python314.zip',
# 'C:\\Users\\samuc\\AppData\\Local\\Programs\\Python\\Python314\\DLLs',
# 'C:\\Users\\samuc\\AppData\\Local\\Programs\\Python\\Python314\\Lib',
# 'C:\\Users\\samuc\\AppData\\Local\\Programs\\Python\\Python314',
# 'C:\\Users\\samuc\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages']

# sys.path.append('\home')
# print('este módulo se chama: ', __name__)
# print(*sys.path, sep='\n')
# c:\Users\samuc\Desktop\teoria\teoria
# C:\Users\samuc\AppData\Local\Programs\Python\Python314\python314.zip
# C:\Users\samuc\AppData\Local\Programs\Python\Python314\DLLs
# C:\Users\samuc\AppData\Local\Programs\Python\Python314\Lib
# C:\Users\samuc\AppData\Local\Programs\Python\Python314
# C:\Users\samuc\AppData\Local\Programs\Python\Python314\Lib\site-packages

# este módulo se chama:  modularizaçao_m
# este módulo se chama:  __main__

import modularizaçao_m
from modularizaçao_m import variavel_modulo, soma


print(modularizaçao_m.variavel_modulo)
print(variavel_modulo)
print(soma(3, 5))
print(modularizaçao_m.soma(4, 7))