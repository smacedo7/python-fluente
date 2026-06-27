def geradora():
    i = 0
    while True:
        yield i
        i += 1

g = geradora()
next(g)

for i in geradora():
    print(i)