from itertools import permutations

# This version work using permutations function for check in loop all symbols
# The code works only with short words and is not very efficient.

def list_position(word):
    s = set()
    sorted_string = sorted(word)
    perms = permutations(sorted_string)
    k = 0
    for el in perms:
        item = ''.join(el)
        if item in s:
            continue
        k += 1
        s.add(item)
        if item == word:
            return k


if __name__=='__main__':
    print(list_position('ABAB'))
    print(list_position('AAAB'))
    print(list_position('BAAA'))
    # print(list_position('YTTSRONLIIAA'))
    # print(list_position('QUESTION'))
    # print(list_position('BOOKKEEPER'))
