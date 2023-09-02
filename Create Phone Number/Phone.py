from os import sep
from re import I


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#0
print('(' + "".join(map(str, n[0:3])) + ') ' + "".join(map(str, n[3:6])) + '-' + "".join(map(str, n[6:10])) )


#1
phone = ''
for i, a in enumerate(n):
    if i == 0:
        separetor = '('
    elif i == 3:
        separetor = ') '
    elif i == 6:
        separetor = '-'
    else:
        separetor = ''
    phone = phone + separetor + str(a)        
# phone = ''.join(map(str, n))
print(phone)

#2
phone2 = "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
print(phone2)

#3
str1 =  ''.join(str(x) for x in n[0:3])
str2 =  ''.join(str(x) for x in n[3:6])
str3 =  ''.join(str(x) for x in n[6:10])
print('({}) {}-{}'.format(str1, str2, str3))

#4
print("(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n))
