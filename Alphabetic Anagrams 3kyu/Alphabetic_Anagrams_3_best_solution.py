from icecream import ic
from math import factorial
from itertools import permutations
import time
from decimal import Decimal

# This version of the function still works even if the characters in a word are repeated.

def list_position(word):
    # Print all variantions using permutation function for check answer
    # Don't use for long words
    # sorted_word = sorted(word)
    # perms = set(permutations(sorted_word))
    # ic(sorted(perms)) 

    unic_letters = set(word) # Get just unique letters

    def all_possible_variants(word):
        variants = factorial(len(word)) # Factorial of word length
        for b in unic_letters:
            variants //= factorial(word.count(b))
        return variants

    count = all_possible_variants(word) # Initialize the counter with the maximum possible number of permutations in a word

    for key, a in enumerate(word):
        # Сount the number of possible options making the word shorter for each pass
        all_variants = all_possible_variants(word[key:]) 

        for b in word[key:]:
            if a < b:
                # if the previous character is less than the next one
                # Substruct from the counter the quotient of all possible options and the remaining length of the word
                count -= Decimal(all_variants)/Decimal(len(word[key:]))
                # I used Decimal because Float's accuracy is not enough
    
    return int(count)


if __name__=='__main__':
    t0 = time.time()

    ic(list_position('ABAB'))
    ic(list_position('ABC'))
    ic(list_position('IMMUNOELECTROPHORETICALLY')) # 718393983731145698173
    ic(list_position('RIHZYJUQZFASRDHOYZMTGJLYH')) # 10490477337540115734010
    ic(list_position('LUNGWGFTQTEOLGWYQECLMYTCI')) # 1027085538706247306471

    t1 = time.time()
    code_speed = t1-t0
    ic(code_speed)