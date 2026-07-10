# __add__ define o comportamento do + 
# um objeto nao nasce com nenhum metodo
# entao precisamos cria-los
# quando fazemos 2 + 3
# na pratica estamos fazendo int.__add__(2, 3)
# ou quado fazemos "oi" + "tudo bem"
# acontece algo do tipo __str__.__add__("Oi", "Tudo bem")
# metodos significam funcs dentro de classes
# sempre que colocamos pontos estamos usando metodos
# quando usamos o mais ativamos o operador do __add__ 

oi = "oi"
print(oi.__class__.__name__)  # str é a classe de oi 
print(type(oi))  # class str, o type mostra a classe

# usar quando houver uma soma logica entre dois objetos
# se o python ver por exemplo dos objetos v1 e v2
# fazendo v1 + v2, procura na classe deles o metodo __add__
# se existir execute, se nao da typeError
# define o comportamento de + 
# sempre recebe self e outro
# retornar um objeto novo

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        
        return Vetor(novo_x, novo_y)

    def __repr__(self):
        return f"Vetor x=({self.x}, y=({self.y}))"
    

v1 = Vetor(2, 3)
v2 = Vetor(4, 5)
v3 = v1 + v2
print(v3)

# quando escreve a + b, ta fazendo:
# a.__add__(b)