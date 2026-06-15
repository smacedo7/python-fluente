# abstraçao: abstração: focar apenas no que importa para aquele momento,
# ignorando os detalhes internos.
# log
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):  # assinatura do metodo, metodo abstrato
        raise NotImplementedError(
            'Implemente o método log'
        )

    def log_error(self, msg):  # metodo concreto
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg}, {self.__class__.__name__}')


class LogFileMixin(Log):  # classe com funcionalidades que serao add
    # a outras classes
    def _log(self, msg):  # como estamos sobrepondo o metódo, a assinatura deve ser identica
        print(msg)
        msg_fomatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_fomatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_fomatada)
            arquivo.write('\n')


if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('qualquer coisa')
    l.log_success('Que legal')
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('Que legal')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')

# "Qualquer classe que herdar de mim PRECISA implementar _log()."
# "Filho, você é obrigado a sobrescrever esse método."