import re


pin = '1234'

#1
def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        return pin.isnumeric()
    else:
        return False

#2
def validate_pin2(pin):
    return len(pin) in (4, 6) and pin.isdigit()


#3
def validate_pin3(pin):
    #return true or false
    return bool(re.fullmatch("\d{4}|\d{6}", pin))


#4
def validate_pin4(pin):
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)

print(validate_pin(pin))