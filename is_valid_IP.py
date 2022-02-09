import re

strng = '123.456.789.0'

def is_valid_IP(strng):
    answer = 0
    num = ''
    ip_num = {}
    idx = 0
    for el in strng:
        if el.isnumeric():
            num += el 
        else:
            num = ''
            idx += 1 # сделать проверку на количество октетов
        ip_num[idx] = num
    print(ip_num)
    for x in ip_num:
        print(x)
        if x >= 0 or x < 255 or str(x)[0] != 0:
            answer ^= 1
            print('x ', x)
            print('answer ', answer)
    
    return bool(answer)


print(is_valid_IP(strng))