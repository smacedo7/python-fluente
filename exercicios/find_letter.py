def find_letter(lista):
    n = 0
    while ord[lista[n]] == ord(lista[n + 1]) - 1:
        n += 1
    return chr(ord(1 + ord(lista[n])))