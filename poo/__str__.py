# o python tem ordem de preferencia:
# existe __str__ -> sim; usa __str__
# se nao tiver, usa __repr__ 
# se implementar so __reprt__, o print(objeto)
# continua funcionando pq ele usa o repr como fallback
# em sistemas de verdade, procurar usar os dois

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vetor x=({self.x}, y=({self.y}))"
    
v1 = Vetor(2, 3)
print(v1)  # vai printar o __Str__ (2, 3)
print([v1])  # vai printar o __repr__ [Vetor x=(2, y=(3))]
print(v1.x)
print(v1.y)
print(v1.__str__)  # <bound method Vetor.__str__ of Vetor x=(2, y=(3))>
print(str(v1))  # (2, 3)
print(repr(v1))  # Vetor x=(2, y=(3))

# __str__ representacao util para pessoas
# enquanro __repr representacao util para devs