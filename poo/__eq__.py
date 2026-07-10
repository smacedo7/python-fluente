# define o comportamento de ==;
# objeto1 == objeto2;
# objeto1.__eq__(objeto2);
# usar quando 2 objetos diferentes seguirem o mesmo valor logico
# passa a classe pra verificar se é uma instancia de classe

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, value):
        if not isinstance(value, Vetor):
            return False
        
        return self.x == value.x and self.y == value.y
    
    def __repr__(self):
        return f"Vetor ({self.x}, {self.y})"

v1 = Vetor(2, 3)
v2 = Vetor(4, 5)
v3 = False
v4 = Vetor(2, 3)

print(v1 == v4)  # True
print(v1 == v2)  # False
print(v1 == v3)  # False