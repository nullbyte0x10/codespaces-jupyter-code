import dfa
from dfa import DFA


def testDFA():
    # Test strings that belong to the first language
    assert DFA("aa") == 2
    assert DFA("baa") == 2
    assert DFA("ababaa") == 2
    assert DFA("bbbabaa") == 2

    # Test strings that belong to the second language
    assert DFA("aba") == 4
    assert DFA("babab") == 4
    assert DFA("ababa") == 4
    assert DFA("babaa") == 4

    # Test strings that belong to both languages
    assert DFA("abaabaa") == 4
    assert DFA("ababaabaa") == 4
    assert DFA("baaababa") == 4

    # Test strings that belong to neither language
    assert DFA("") == 0
    assert DFA("a") == 1
    assert DFA("bb") == 3
    assert DFA("ab") == 3
    assert DFA("abb") == 3
    assert DFA("abba") == 3
