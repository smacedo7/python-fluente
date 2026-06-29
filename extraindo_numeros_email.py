import re
import pyperclip


# area de transferencia é onde guarda oq vc copiou
# pyperclip.paste() pega oq ta copiado e armazena no texto


phone_re = re.compile(r'''(
                    (\d{3}|\(\d{3}\))?
                    (\s|-|\.)?
                    (\d{3})
                    (\s|\.|-)
                    (\d{4})
                    (\s*(ext|x|ext\.)\s*(\d{2,5}))?
                    )''', re.VERBOSE)

email_re = re.compile(r'''(
                      [a-zA-Z0-9._-]+
                      @
                      [a-zA-Z0-9._-]+
                      (\.[a-zA-Z]{2, 4})
                      )''', re.VERBOSE)

text = str(pyperclip.paste())  # pega oq eu copiei da area de transferencia

matches = []
for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[2], groups[5]])  # precisa estar
    # dentro de um iteravel
    if groups[6] != '':
        phone_num += ' x' + groups[6]
    matches.append(phone_num)
for groups in email_re.findall(text):
    matches.append(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join(matches))
else:
    print('no phone numbers or email found')
