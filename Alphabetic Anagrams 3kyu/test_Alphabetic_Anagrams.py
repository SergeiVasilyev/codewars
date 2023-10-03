from Alphabetic_Anagrams_1 import list_position

def test_list_position():
    assert(list_position('ABAB') == 2)
    assert(list_position('AAAB') == 1)
    assert(list_position('QUESTION') == 24572)
    assert(list_position('BOOKKEEPER') == 10743)
    assert(list_position('BOOKKEEPERS') == 94027)
    # assert(list_position('BOOKKEEPERASDFG') == 10743)
    # assert(list_position('BOOKKEEPERKJNSJSKJKEJBFQN') == 10743)
