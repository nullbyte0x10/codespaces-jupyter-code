class DFA:
    def __init__(self, alphabet, transitions, start_state, accepting_states):
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accepting_states = accepting_states

    def accepts(self, string):
        state = self.start_state
        for symbol in string:
            state = self.transitions.get((state, symbol))
            if state is None:
                return False
        return state in self.accepting_states


# Example usage
alphabet = set(input("Enter symbols of your alphabet, separated by commas: ").split(','))
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

while True:
    string = input("Enter a string: ")
    if string == 'Q':
        break
    if dfa.accepts(string):
        print("Accepted")
    else:
        print("Rejected")
