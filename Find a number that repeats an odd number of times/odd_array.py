from functools import reduce
import operator

seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]


def find_it(seq):
    counter_arr = {}
    x = None
    for num in seq:
        if num in counter_arr:
            counter_arr[num] += 1
        else:
            counter_arr.update({num: 1})
        # print(num, '->', counter_arr[num])
    for key in counter_arr:
        if counter_arr[key] % 2:
            x = key
    return x

# Запомнить!!!
def find_it2(seq):
    nums = set()
    for num in seq:
        if num in nums:
            nums.remove(num)
            print('remove ', num)
        else:
            nums.add(num)
            print('add ', nums)
    return nums.pop()
# Список Python pop() — это встроенная функция Python, которая удаляет и возвращает последнее значение из списка или заданное значение индекса.


# Элегантное, но не эффективное решение, так как каждый раз за проход цикла count проходит заново по всему массиву
def find_it3(seq):
    for i in seq:
        if seq.count(i) % 2: # .count() возвращает количество вхождений
            return i


# Запомнить!!!
# xor(a, a) = 0 and xor(a, 0) = a. 
# So, when you xor all the numbers, every number with even frequency gets cancelled out and only the number with odd frequence remains.
# Итак, когда вы выполняете операцию xor для всех чисел, каждое число с четной частотой отменяется, и остается только число с нечетной частотой.
def find_it4(xs):
    return reduce(operator.xor, xs)

def find_it4_1(xs):
    def xors(x, y):
        print ('x = ', x, 'y = ', y)
        print ("XOR ", operator.xor(x, y))
        return operator.xor(x, y)

    return reduce(xors, xs)

def find_it4_2(seq):
    result = 0
    for x in seq:
        result ^= x
    return result


print(find_it(seq))