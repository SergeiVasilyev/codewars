from Alphabetic_Anagrams_1 import list_position
from Alphabetic_Anagrams_2 import list_position as list_position2
from Alphabetic_Anagrams_3_best_solution import list_position as list_position3

def test_list_position_1():
    assert(list_position('ABAB') == 2)
    assert(list_position('AAAB') == 1)
    assert(list_position('QUESTION') == 24572)
    assert(list_position('BOOKKEEPER') == 10743)


def test_list_position_2():
    assert(list_position2('ABC') == 1)
    assert(list_position2('CAB') == 5)
    assert(list_position2('BCAD') == 9)
    assert(list_position2('QUESTION') == 24572)
    assert(list_position2('AAAB') != 1)
    assert(list_position2('BABA') != 5)


def test_list_position_3():
    assert(list_position3('ABAB') == 2)
    assert(list_position3('ABAA') == 3)
    assert(list_position3('CAAB') == 10)
    assert(list_position3('QUESTION') == 24572)
    assert(list_position3('BOOKKEEPER') == 10743)
    assert(list_position3('BOOKKEEPERS') == 94027)
    assert(list_position3('BOOKKEEPERASDFG') == 6354519619)
    assert(list_position3('BOOKKEEPERKJNSJSKJKEJBFQN') == 866199282189993890)
    assert(list_position3('IMMUNOELECTROPHORETICALLY') == 718393983731145698173)
    assert(list_position3('RIHZYJUQZFASRDHOYZMTGJLYH') == 10490477337540115734010)
    assert(list_position3('LUNGWGFTQTEOLGWYQECLMYTCI') == 1027085538706247306471)