def isPhoneNumber(text):
    if len(text) != 12:
        return False  # not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # not area code
    if text[3] != '-':
        return False  # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # no first three digits
    if text[7] != '-':
        return False  # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # no three digits
    else: 
        return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
for i in range(len(message)):
    segment = message[i:i+12]
    if isPhoneNumber(segment):
        print('Phone number found: ' + segment)
print("done")