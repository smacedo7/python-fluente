# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):  # esquerda é o p1 e direita p2
        novo_x = self.x + other.x  # p1.x + p2.x
        novo_y = self.y + other.y  # p1.y + p2.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):  # GT = Greater Than
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


if __name__ == '__main__':
    p1 = Ponto(4, 2)  # 6
    p2 = Ponto(6, 4)  # 10
    p3 = p1 + p2  # quando faz isso aciona o dunder method
    print(p3)
    print('P1 é maior que p2', p1 > p2)
    print('P2 é maior que p1', p2 > p1)
    print((p1).__gt__(p2))  # False

print((10).__add__(20))  # 30

# Sim. Se tu quer usar + entre objetos da
# tua classe, precisa implementar __add__.