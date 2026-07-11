class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Vetor(new_x, new_y)

    def __eq__(self, value):
        if not isinstance(value, Vetor):
            return NotImplemented
        # if self.x == value.x and self.y == value.y:
        #     return True
        # else:
        #     return False
        return self.x == value.x and self.y == value.y
    
    def __len__(self):
        # return len([self.x, self.y])  # nao necesasriamente precisava retornar um len
        # mas sempre um numero inteiro
        return 2
    
    def __repr__(self):
        return f"Vetor: (x={self.x}, y={self.y})"
    
v1 = Vetor(2, 3)
v2 = Vetor(5, 7)
v3 = Vetor(2, 3)
v4 = Vetor(3, 2)

print("=== __repr__ ===")
print(v1)
print(v2)

print("\n=== __add__ ===")
resultado = v1 + v2
print(resultado)

print("\n=== __eq__ ===")
print(v1 == v2)   # False
print(v1 == v3)   # True
print(v1 == v4)   # False

print("\n=== __len__ ===")
print(len(v1))
print(len(v2))

print("\n=== Objetos originais ===")
print(v1)
print(v2)

# print("\n=== Desafio ===")
# print(v1 + 10)