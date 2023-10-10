from icecream import ic
from math import factorial
from itertools import permutations
import time

# This version of the function works if there are no repeating characters in the word

def list_position(word):
    # Print all variantions using permutation function for check answer
    # Don't use for long words
    # sorted_word = sorted(word)
    # perms = set(permutations(sorted_word))
    # ic(sorted(perms))

    all_variants = factorial(len(word))
    count = all_variants

    for key, a in enumerate(word):
        for b in word[key:]:
            all_variants = factorial(len(word[key:]))
            if a < b:
                count -= all_variants/len(word[key:])
    
    return count



if __name__=='__main__':
    t0 = time.time()

    ic(list_position('BAC'))
    ic(list_position('BCDA'))

    t1 = time.time()
    code_speed = t1-t0
    ic(code_speed)