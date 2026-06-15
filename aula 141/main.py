from log import LogFileMixin, LogPrintMixin


l = LogPrintMixin()
l.log_error('qualquer coisa')
l.log_success('Que legal')
lp = LogPrintMixin()
lp.log_error('qualquer coisa')
lp.log_success('Que legal')
lf = LogFileMixin()
lf.log_error('qualquer coisa')
lf.log_success('Que legal')