from dfa import DFA
def test_dfa():
    alphabet = {'a', 'b'}
    transitions = {
        (1, 'a'): 2,
        (1, 'b'): 1,
        (2, 'a'): 3,
        (2, 'b'): 1,
        (3, 'a'): 3,
        (3, 'b'): 4,
        (4, 'a'): 4,
        (4, 'b'): 4,
    }
    start_state = 1
    accepting_states = {4}

    dfa = DFA(alphabet, transitions, start_state, accepting_states)

    assert dfa.accepts("abaabaa")
    assert not dfa.accepts("aaba")
    assert dfa.accepts("aaaaaa")
    assert not dfa.accepts("abababa")
    assert not dfa.accepts("")
    assert dfa.accepts("aba")
    assert dfa.accepts("babaabaa")
