def find_even_index(arr):
    for i, el in enumerate(arr):
        left = arr[0: i]
        right = arr[i+1:]
        if sum(left) == sum(right):
            return i
    return -1


if __name__=='__main__':
    print(find_even_index([1,2,3,4,3,2,1]))