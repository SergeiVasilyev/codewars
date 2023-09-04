import operator
from functools import reduce

def array_diff(a, b):
    b_no_duplicate = set(b) # Delete duplicates in b
    for b_el in b_no_duplicate:
        # a = list(filter(lambda x: x != b_el, a)) # Version with filter
        a = [a_el for a_el in a if a_el != b_el] # Version with for loop

    return a

# Second version
def array_diff2(a, b):
    b_no_duplicate = set(b)
    a = [a_el for a_el in a if a_el not in b_no_duplicate]
    return a

if __name__ == '__main__':
    print(array_diff([1,2,2,3],[1,2]))
