class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return 
    
    def __eq__(self, value):
        pass

    def __len__(self):
        return len(self)

v1 = Vetor(2, 3)
v2 = Vetor(5, 7)
print(v1)
v3 = v1 + v2

print(v3.x)
print(v3.y)