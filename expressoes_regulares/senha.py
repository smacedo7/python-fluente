import humre
import pyperclip
import re

maiuscula = re.compile(r'[A-Z]')
minuscula = re.compile(r'[a-z]')
numero = re.compile(r'\d')

senha = ''
if len(senha) >= 8:
    if maiuscula.search(senha) and minuscula.search(senha) and numero.search(senha):
        print('a senha é segura')
    else:
        print('senha invalida! ')
