import re

strng = '123.456.758.0'
strng = '123.125.789.123'

# 1 Решение без регулярных выражений, не самое элегантное
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
            idx += 1
        ip_num[idx] = num

    print(f"idx {idx}")
    if idx != 3: # Если октетов меньше 4, то сразу возвращаем False
        return False

    for x in ip_num:
        print(ip_num[x])
        # Если число в диапазоне от 0 до 255 и при этом каждое число не должено начинаться с 0.
        if int(ip_num[x]) >= 0 and int(ip_num[x]) <= 255 and not (int(str(ip_num[x])[0]) == 0 and len(ip_num[x]) == 1):
            answer += 1
            print('0 symbol ', str(ip_num[x])[0])
            print('answer ', answer)

    answer ^= 4
    print('final answer ', not answer)
    return not bool(answer)

# strng = '12.255.56.1'

# 2 Мой вариант с коммандой SPLIT
def is_valid_IP2(strng):
    lt = strng.split(".")
    answer = 0
    for x in lt:
        # if x.isnumeric() and (len(x) > 1 and x[0] != '0' or len(x) == 1) and int(x) <= 255:
        if x.isnumeric() and x == str(int(x)) and 0 <= int(x) <= 255:
            # На 0 вначале можно проверить таким образом x != str(int(x)), при переводе в число 0 вначале уходит и соответсвенно строки перестают быть равными
            answer += 1
            print(x)
    answer ^= 4
    print (not bool(answer))
    return lt

# strng = '255.0.1.75'

# 3 Мой вариант с регулярным выражением
def is_valid_IP3(strng):
    # 0 либо (1-9 1 раз, либо 1-9 + 0-9 1 раз, либо 1-9 + 0-9 2 раза, либо 2 + 0-4 + 0-9, либо 2 + 0-5 + 0-5)
    result = re.match(r'((0{1}|([1-9]{1}|[1-9]\d{1}|[1]\d{2}|[2][0-4]\d|[2][0-5][0-5]))\.){3}(0{1}|([1-9]{1}|[1-9]\d{1}|[1]\d{2}|[2][0-4]\d|[2][0-5][0-5]))$', strng) 
    print (bool(result))
    return result


# 4 Вариант с codewars
def is_valid_IP4(s):
    return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))

# 5 Вариант с codewars
def is_valid_IP5(strng):
    octets = strng.split('.')
    if len(octets) != 4:
        return False
    
    for octet in octets:
        try:
            if octet.count(' ') or octet.startswith('0') or int(octet) > 255 or int(octet) < 0:
                return False
        except:
            return False
    
    return True

# 6 Вариант с codewars
def is_valid_IP6(address):
    return bool(__import__('re').match('(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}\Z',address))

# 7 Вариант с codewars
def is_valid_IP(string):
    m = re.match(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', string)
    if not m:
        return False
    octets = m.groups()
    if any(str(int(octet)) != octet for octet in octets):
        # Removes extra verbose numbers
        return False
    return all( 0<= int(octet) < 256 for octet in octets)


print(is_valid_IP2(strng))