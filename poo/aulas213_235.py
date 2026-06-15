# from os import system


# class Caneta:
#     def __init__(self, cor):
#         # private, protected
#         self.cor_tinta = cor

#     @property
#     def cor(self):
#         return self.cor_tinta


# c1 = Caneta('azul')
# print(c1.cor)  # nao precisa de parenteses
# metodo que age como atributo = propherty
# getter - obter valor
# c1.cor = 'rosa' # nao vai funcionar pq metodo
# nao armazena valor


# class Caneta2:
#     def __init__(self, cor, cor_da_tampa):
#         self._cor = cor
#         self._cor_da_tampa = cor_da_tampa

#     @property
#     def cor(self):
#         return self._cor

#     @cor.setter
#     def cor(self, valor):
#         self._cor = valor

#     @property
#     def cor_da_tampa(self):
#         return self._cor_da_tampa

#     @cor_da_tampa.setter
#     def cor_da_tampa(self, valor):
#         self.cor_da_tampa = valor


# caneta1 = Caneta2('azul', 'azul escura')
# print(caneta1.cor)
# caneta1.cor = 'rosa'
# print(caneta1.cor)
# print(caneta1.cor_da_tampa)
# caneta1.cor_da_tampa = 'rosinha'
# print(caneta1.cor_da_tampa)

# estrutura vai ser sempre properthy
# getter que retorna valor
# e setter que armazena valor


# class Foo:
#     def __init__(self):
#         self.public = 'isso é publico'
#         self._protect = 'isso é protegido'
#         self.__private = 'isso é privado'

#     def metodo_public(self):
#         self.__metodo_private()
#         return self.public

#     def _metodo_protect(self):
#         return self._protect

#     def __metodo_private(self):
#         print('metodo private')
#         return self.__private


# c1 = Foo()
# print(c1._Foo__private)  # primeiro da erro depois pede
# # pra alterar e mostra que é privado
# print(c1.metodo_public())

class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('metodo A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('metodo B')


class C(B):
    atributo_c = 'valor c'

    # def __init__(self, atributo, outra_coisa):
    #     super().__init__(atributo, outra_coisa)
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def metodo(self):
        super().metodo()  # b
        # super(B, self).metodo()  # A      
        # super(A, self).metodo()  # object 
        A.metodo()
        B.metodo()


c = C('Atributo', 'qualquer coisa')
print(c.atributo)
