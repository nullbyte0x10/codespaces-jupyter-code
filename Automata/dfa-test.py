from dfa import dfa
def test_dfa():
    # Test strings that belong to the first language
    assert dfa("aa") == 2
    assert dfa("baa") == 2
    assert dfa("ababaa") == 2
    assert dfa("bbbabaa") == 2
    
    # Test strings that belong to the second language
    assert dfa("aba") == 4
    assert dfa("babab") == 4
    assert dfa("ababa") == 4
    assert dfa("babaa") == 4
    
    # Test strings that belong to both languages
    assert dfa("abaabaa") == 4
    assert dfa("ababaabaa") == 4
    assert dfa("baaababa") == 4
    
    # Test strings that belong to neither language
    assert dfa("") == 0
    assert dfa("a") == 1
    assert dfa("bb") == 3
    assert dfa("ab") == 3
    assert dfa("abb") == 3
    assert dfa("abba") == 3
