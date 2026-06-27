try:
    print("1. Tentando executar o bloco try...")
    resultado = 10 / 2
except ZeroDivisionError:
    print("2. Ocorreu uma divisão por zero! (Isso não vai rodar)")
else:
    print("2. Nenhum erro ocorreu. Bloco else executado!")
finally:
    print("3. O bloco finally é sempre executado no final!")

# 1. Tentando executar o bloco try...
# 2. Nenhum erro ocorreu. Bloco else executado!
# 3. O bloco finally é sempre executado no final!