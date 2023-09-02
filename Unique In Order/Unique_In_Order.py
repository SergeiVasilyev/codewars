# iterable = [1,2,2,3,3] 
iterable = 'AAAABBBCCDAABBB'
# iterable = []

#1 my
def unique_in_order(iterable):
    arr = []
    if iterable:
        arr.append(iterable[0])
        for i, sym in enumerate(iterable):
            if not iterable[i] == arr[-1] and i != 0:
                arr.append(sym)
    return arr

#2
def unique_in_order2(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

#3 !
def unique_in_order3(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res


#4
unique_in_order5 = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]


print (unique_in_order5(iterable))