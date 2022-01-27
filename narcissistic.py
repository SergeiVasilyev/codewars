value = 371

def narcissistic( value ):
    test_num = 0
    length = len(str(value))
    for digit in str(value):
        test_num += int(digit)**length
    return not bool(test_num-value)

def narcissistic2(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))

def narcissistic3( value ):
    v = value
    l = len(str(value))
    s = 0
    while v > 0:
        print('v = ', v)
        s += (v % 10)**l
        print('s = ', s)
        v //= 10    
    return s == value



print (narcissistic(value))