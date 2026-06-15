from log import LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligaar(self):
        if self._ligado:
            self._ligado = False


class Smartphonme(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()  # nao sobreescreve o metodo de desligar
        # "Executa o ligar da classe pai primeiro."

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)