class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):

    @staticmethod
    def falar():
        return "Au Au!"

class Gato(Animal):
    
    @staticmethod
    def falar():  # poderia passar o self aqui, mas preferi deixar o static method
        # agora se alguem herdar de cachorro acho que fica mais complicado pq nao vai ter o self ali
        return "Miau!"
    
dog = Cachorro('mike')
print(dog.nome)  # como cachorro herda de animal,
# ele tem um nome visto que animal tambem tem um nome no seu init

cat = Gato("Mimi")


print(dog.falar())

print(cat.nome)
print(cat.falar())

# cachorro nao tem init, entao procura na classe pai
# herança é feita pra reutilizaçao de codigo.
# colocar o self la dentro pq o cachorro latiu que é a instancia
# nao a classe latiu.