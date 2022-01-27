arr = [ 1, 1, 1, 2, 1, 1 ]

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

print(find_uniq(arr))