from dfa import DFA
import unittest

class DFATests(unittest.TestCase):
    def test_accepts_valid_strings(self):
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

        self.assertTrue(dfa.accepts('aaab'))
        self.assertTrue(dfa.accepts('baaab'))
        self.assertTrue(dfa.accepts('aaabab'))
        self.assertTrue(dfa.accepts('aabab'))
        self.assertTrue(dfa.accepts('aaababab'))
        self.assertTrue(dfa.accepts('aaabababab'))
        self.assertTrue(dfa.accepts('aaaaabab'))
        self.assertTrue(dfa.accepts('aaaaaaabab'))

    def test_rejects_invalid_strings(self):
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

        self.assertFalse(dfa.accepts(''))
        self.assertFalse(dfa.accepts('a'))
        self.assertFalse(dfa.accepts('ab'))
        self.assertFalse(dfa.accepts('aaa'))
        self.assertFalse(dfa.accepts('aaaa'))
        self.assertFalse(dfa.accepts('aabaa'))
        self.assertFalse(dfa.accepts('aabb'))
        self.assertFalse(dfa.accepts('baa'))
