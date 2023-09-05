# My first solution
def find_outlier(integers):
    def is_more_odd_numbers_in_list(x):
        odd = 0
        for y in x:
            if y % 2:
                odd += 1
        return True if odd >= 2 else False
    is_odd = is_more_odd_numbers_in_list(integers[:3])
    
    for n in integers:
        if n % 2 ^ is_odd:
            return n
        
        
# My second solution (refactor)
def find_outlier2(integers):
    def is_more_odd_numbers_in_list(x):
        return True if len([y for y in x if y % 2]) >= 2 else False
    is_odd = is_more_odd_numbers_in_list(integers[:3])

    for n in integers:
        if n % 2 ^ is_odd:
            return n
        


# Interesting solution from Codewars
def find_outlier3(integers):
    assert len(integers) >= 3

    # Четные всегда заканчиваются на 0, а нечетные на 1
    # Поэтому применяя AND 1 узнаем четное или нечетное
    bit = ((integers[0] & 1) +
        (integers[1] & 1) +
        (integers[2] & 1)) >> 1

    for n in integers:
        if (n & 1) ^ bit:
            return n

    assert False



# My new solution is based on the previous solution from codewords
def find_outlier4(integers):
    is_odd = sum(map(lambda a: a % 2, integers[:3])) >> 1
    for n in integers:
        if n % 2 ^ is_odd:
            return n


if __name__=='__main__':
    print(find_outlier4([2, 3, 8, 100, 4, 6, 2602, 36])) # Should return: 3
    print(find_outlier4([2, 46, 8, 100, 4, 6, 2601, 36])) # Should return: 2601
    print(find_outlier4([5, 55, 97, 21, 3, 9, 101, 31, 29, 56])) # Should return: 56
    print(find_outlier4([5, 4, 97, 21, 3, 9, 101, 31, 29, 55])) # Should return: 4

