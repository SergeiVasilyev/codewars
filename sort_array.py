# Отсортировать все нечетные числа не меняя расположение четных
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
import re


source_array = [5, 8, 6, 3, 4]

# 1
def sort_array(source_array):
    array = []
    for el in source_array:
        if el % 2:
            array.append(el)
    array.sort()
    print(array)
    for i, el in enumerate(source_array):
        if el % 2 and array:
            source_array[i] = array[0]
            array.pop(0)
    
    return source_array

# 2 не работает, попытка написать в одном цикле
def sort_array2(source_array):
    source_array2 = source_array.copy()
    source_array2.sort()
    print(source_array2)
    x = lambda array: [el for el in array if el % 2]
    print('x ', x(source_array))
    y = lambda array: [array[i] for i, el in enumerate(array) if el % 2 and x]
    print('y ', y(source_array))
    return source_array

# 3
def sort_array3(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    # for n in odds:
    #     print(n)
    return [next(odds) if i % 2 else i for i in source_array]

# 4
def sort_array4(source_array):
    a = list(filter(lambda x: x % 2, source_array))
    a.sort()
    print(a)
    for i in range(len(source_array)):
        if not source_array[i] % 2:
            print(source_array[i])
            a.insert(i, source_array[i]) # вставляет элемент по указанному индексу, сдвигая существующее вправо.
    return a

# Проверка на четность, повтор
def sort_array5(source_array):
    print('--Проверка на четность--')
    for el in source_array:
        print (el & 1)
    print('--Проверка на четность--')
    for el in source_array:
        print (el % 2)

    print('--Проверка на повтор--')
    for el in source_array:
        print (el ^ el) # Проверка на повтор. Если сравниваются 2 одинаковых числа возвращает 0, иначе если сравнивается с 0 -м возвращает исходное значение

print(sort_array(source_array))

