from pathlib import Path
import os

print(Path.cwd())  # /Users/samuelmacedo/Projetos/python/python-fluente
atual = Path.cwd()
print(atual)  # /Users/samuelmacedo/Projetos/python/python-fluente
os.chdir('/Users/samuelmacedo/Projetos/python/python-fluente/arquivos')
print(Path.cwd())  # /Users/samuelmacedo/Projetos/python/python-fluente/arquivos