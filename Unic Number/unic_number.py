arr = [ 1, 1, 1, 2, 1, 1 ]
arr = [ 1, 1, 1, 2, 1, 1, 2, 50, 25, 50 ]
arr = [ 0, 0, 0.55, 0, 0 ]

# 1 My
def find_uniq(arr):
    counter_arr = {}
    print (counter_arr)
    for i, x in enumerate(arr):
        if x in counter_arr:
            counter_arr[x] = counter_arr[x] + 1
        else:
            counter_arr.update({x: 1})
        print(x, '->', counter_arr[x])

    print (counter_arr)
    
    # print(sorted(xn, key=lambda x: abs(x - 4))[0]) # находит ближайщее число к 4

    # n = min(counter_arr.values(), key=lambda i: counter_arr[i])
    n = min(counter_arr.items(), key=lambda x: x[1])
    print (n)

    return n[0]   # n: unique number in the array



# 2 My. На codewars ошибка - превышен лимит. с большими массиывми видимо работает медленно
# Работает медленно так как каждый раз в цикле count перебирает массив целиком. 
def find_uniq2(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
# Each time you call the count method, it needs to parse the whole list to count the number of elements matching its argument.
# You do that for every element, that's an aweful thing in terms of efficiency.
# If your list has 10 elements, your code needs to perform 100 operations (10 * 10).
# If your list has 1000 elements, 1,000,000 (1000 * 1000).
# And so on. It's easy to understand that with a large list that becomes incredibely huge.
# That's why it is said to be inefficient. You need to find a better approach.


print(find_uniq2(arr))