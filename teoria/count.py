from itertools import count

c1 = count()  # pode passar o inicio tipo count(10)
r1 = range(100)  # range tem fim
print(next(c1))
print(next(c1))

print('c1', hasattr(c1, '__iter__'))  # possui o metodo iter, é iteravel

print('c1', hasattr(c1, '__next__'))  # é iterator

print('r1', hasattr(r1, '__iter__'))  # possui o metodo iter, é iteravel

print('r1', hasattr(r1, '__next__'))  # nao é iterator

print('count')
for i in c1:
    if i > 100:
        break
    print(i)

print()
print('range')
for i in r1:
    if i > 100:
        break
    print(i)
