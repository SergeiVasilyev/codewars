# 1 solution from codewars
# https://www.codewars.com/kata/reviews/5419c648c01d84810b00016e/groups/54590653cbae2acf3d0006ab

from collections import Counter

def listPosition(word):
    l, r, s = len(word), 1, 1
    c = Counter()

    for i in range(l):
        x = word[(l - 1) - i]
        c[x] += 1
        for y in c:
            if (y < x):
                r += s * c[y] // c[x]
        s = s * (i + 1) // c[x]
    return r
# ---------------------------------------------


# 2 solution from stackoverflow
# https://stackoverflow.com/questions/69114938/alphabatic-anagrams-doesnt-work-with-words-that-contains-letters-with-multiple
# I replaced division with integer division because otherwise there is not enough precision for long words

from math import factorial
import time


def list_position(word):
    count = 0
    while len(word):
        first = word[0]
        uniqs = set(word)
        possibles = factorial(len(word))
        
        for ch in uniqs:
            possibles //= factorial(word.count(ch))
            print(factorial(word.count(ch)), 'possibles', possibles)
            
        for ch in uniqs:
            if ch < first: 
                count += possibles // len(word) * word.count(ch)
                print(word, possibles, len(word), word.count(ch), ch, 'count', count)
        word = word[1:]
        
    return count + 1

t0 = time.time()

if __name__=='__main__':
    # print(list_position('IMMUNOELECTROPHORETICALLY'))
    print(list_position('ABAB'))
    # print(list_position('ABBA')) # AABB 1234, BBAA 4321, ABAB 1324
    # print(list_position('AAAB'))
    # print(list_position('BAAA'))
    # print(list_position('ABC'))
    # print(list_position('ACB'))
    # print(list_position('BAC'))
    # print(list_position('YTTSRONLIIAA'))
    # print(list_position('QUESTION'))
    # print(list_position('BOOKKEEPER'))
    # print(list_position('ASDJFGDHBVKKDHSBFJDPEMB'))

t1 = time.time()
total = t1-t0
print(total)