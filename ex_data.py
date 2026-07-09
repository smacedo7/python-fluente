from datetime import datetime

# class Data:
#     def __init__(self, dia, mes, ano):
#         self.dia = dia
#         self.mes = mes
#         self.ano = ano

#     @classmethod
#     def hoje(cls):
#         today = datetime.now()[11]
#         dia = (today.split("-"))[2]
#         mes = (today.split("-"))[1]
#         ano = (today.split("-"))[0]

#         return cls(dia, mes, ano)

#     def __str__(self):
#         if self.dia < 10:
#             self.dia = "0" + str(self.dia)
#         if self.mes < 10:
#             self.mes = "0" + str(self.mes)
#         return f"{self.dia}/{self.mes}/{self.ano}"

# d1 = Data(9, 7, 2007)
# print(d1)
# d2 = Data.hoje()
# print(d2)
# print(datetime.now())

# class Data:
#     def __init__(self, string):
#         self.dia = str(string[0:11].split("-")[2])
#         self.mes = str(string[0:11].split("-")[1])
#         self.ano = str(string[0:11].split("-")[0])

# # d1 = Data.hoje()
# # d2 = Data(9, 7, 2026)
# # print(d2)
# # print(datetime.now())
# print(datetime.now())
# d1 = Data(datetime.now())

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    @classmethod
    def dia(cls):
        now = datetime.now()  # datetime é a classe, now o metodo. a gente importa o modulo
        # e de la tira a classe, agora instanciamos e fizemos now virar um objeto, recebendo
        # os atributos da classe datetime hahahaha

        return cls(now.day, now.month, now.year)  # sao atributos de datetime

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"


d1 = Data(9, 7, 2026)
d2 = Data.dia()
print(d1)
print(d2)
agora = datetime.now()
print(dir(agora))  # aparecem todos os atributos e metodos
# print(help(datetime))
# print(help(agora))