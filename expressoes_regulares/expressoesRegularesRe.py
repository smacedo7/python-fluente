import re

phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')  # passa string regula
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242')
match_obj.group()
print(match_obj.group())
# 4 passos:
# 1- importar modulo re
# 2- passar a string regex para re.compile() para obter objeto pattern
# 3- passar a string de texto para metodo search() do objeto pattern para
# obter um objeto match
# 4- chamar o metodo group do objeto match para obter a string que corresponde
# ao padrao desejado

# re.compile
# var.search
# var.group