
class DFA:
    def __init__(self, alphabet, transitions, start_state, accept_states):
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def accept(self, string):
        current_state = self.start_state
        for symbol in string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transitions.get((current_state, symbol))
            if current_state is None:
                return False
        return current_state in self.accept_states
alphabet = {'a', 'b'}
transitions = {
    (0, 'a'): 1,
        (0, 'b'): 0,
            (1, 'a'): 1,
                (1, 'b'): 2,
                    (2, 'a'): 3,
                        (2, 'b'): 0,
                            (3, 'a'): 1,
                                (3, 'b'): 4,
                                    (4, 'a'): 4,
                                        (4, 'b'): 4
                                        }
start_state = 0
accept_states = {4}

                                        ddfddffafa  ddddfddffaal     ddfddffa  ddddddddfdddddddfddffaddddddddfddddaddddddddfdddddddfddffaddddddddfdddd(alphabet, transitions, start_state, accept_states)
