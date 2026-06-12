a = 8
b = 0
try:
    c = a/b
    print(1)
except ZeroDivisionError as e:
    print(e)
    print(e.__class__.__name__)
    print('dividiu por zero')
finally:
    print(2)